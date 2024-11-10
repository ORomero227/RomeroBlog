from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms.fields.simple import EmailField, PasswordField, SubmitField, StringField, URLField, TextAreaField
from wtforms.validators import DataRequired, Email, URL


class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Login")


class RegisterForm(FlaskForm):
    name = StringField(label="Your Name", validators=[DataRequired()])
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Register")


class CreatePostForm(FlaskForm):
    title = StringField(label="Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    body = CKEditorField(label="Blog Content", validators=[DataRequired()])
    img_url = URLField(label="Post Image URL", validators=[DataRequired(), URL()])
    card_img_url = URLField(label="Presentation Card Image URL", validators=[DataRequired(), URL()])
    submit = SubmitField(label="Save Post")

class CreateCommentForm(FlaskForm):
    comment_text = TextAreaField(label="Comment", validators=[DataRequired()])
    submit = SubmitField(label="Submit Comment")