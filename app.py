import os

from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, login_user, current_user, logout_user
from flask_ckeditor import CKEditor
from werkzeug.security import check_password_hash, generate_password_hash
from database import db, User, BlogPost, Comment
from dotenv import load_dotenv
from forms import LoginForm, RegisterForm, CreatePostForm, CreateCommentForm
from functools import wraps
from datetime import date
from example_data import db_load_example_data

load_dotenv()
login_manager = LoginManager()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Bootstrap5(app)
login_manager.init_app(app)
ckeditor = CKEditor(app)


#------ DATABASE SETTINGS AND CREATING TABLES -------------------
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
db.init_app(app)

with app.app_context():
    db.create_all()
    db_load_example_data(db)


#-------- AUTHENTICATION SETTINGS AND  ROUTES --------------
# Create an admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for("login"))
        elif not check_password_hash(user.password, form.password.data):
            flash("The password is incorrect")
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for("home"))
    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Check if the email is already register
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login"))

        # Hashing the password
        hashed_password = generate_password_hash(form.password.data, method="pbkdf2:sha256")
        new_user = User(
            name = form.name.data,
            email = form.email.data,
            password = hashed_password,
        )

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for("home"))
    return render_template("register.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


#------------ HOME ROUTE -----------------------
@app.route("/")
def home():
    all_posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=all_posts)


#----------- BLOG ROUTES -------------------------
@app.route("/post/<int:post_id>", methods=["GET","POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    comment_form = CreateCommentForm()
    if comment_form.validate_on_submit():
        new_comment = Comment(
            text = comment_form.comment_text.data,
            comment_author = current_user,
            parent_post = requested_post
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for("show_post", post_id=requested_post.id, form=comment_form))
    return render_template("post.html", post=requested_post, form=comment_form)


@app.route("/add-post", methods=["GET","POST"])
@admin_only
def add_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_blog_post = BlogPost(
            title= form.title.data,
            subtitle= form.subtitle.data,
            date= date.today().strftime("%B %d, %Y"),
            body= form.body.data,
            img_url= form.img_url.data,
            card_img_url= form.card_img_url.data,
            author= current_user,
        )
        db.session.add(new_blog_post)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    form = CreatePostForm(
        title = post.title,
        subtitle = post.subtitle,
        body = post.body,
        img_url = post.img_url,
        card_img_url = post.card_img_url
    )

    if form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.body = form.body.data
        post.img_url = form.img_url.data
        post.card_img_url = form.card_img_url.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=form, is_edit=True, post_id=post.id)


@app.route("/delete-post/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

