import pytest
from flask import Flask, render_template, request
from utils import *

app = Flask(__name__, template_folder='templates')


@app.route("/")
def general_page():
    posts = get_posts_all()
    return render_template("index.html", posts=posts)


@app.route("/post/<int:post_id>")
def id_page(post_id):
    post = get_post_by_pk(post_id)
    comment = get_comments_by_post_id(post_id)
    return render_template("post.html", post=post, comment=comment)


@app.route("/search/")
def search_page():
    search = request.args.get('s')
    posts = search_for_posts(search)
    return render_template("search.html", posts=posts)


@app.route("/user_feed/<user_name>")
def user_posts(user_name):
    posts = get_posts_by_user(user_name)
    return render_template("user-feed.html", posts=posts)


@app.errorhandler(404)
def pageNotFount(e):
    er = 404
    return render_template('page_error.html', title="Страница не найдена", er=er)


@app.errorhandler(500)
def pageNotFount(e):
    er = 500
    return render_template('page_error.html', title="Страница не найдена", er=er)


app.run()