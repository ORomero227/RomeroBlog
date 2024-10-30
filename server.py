from flask import Flask, render_template
from post import Post
import requests

# Retrieve posts from n:point api
posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
all_posts = []
for post in posts:
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['body'], post['image_url'])
    all_posts.append(post_obj)

app = Flask(__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=all_posts)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = None
    for blog_post in all_posts:
        if blog_post.id == post_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)