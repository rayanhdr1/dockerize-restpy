from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Page indexe'

@app.route('/hello')
def hello():
    return 'Bonjour à vous'

from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'Utilisateur {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post_int(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}, {type(post_id)}'

@app.route('/autre/<post_id>')
def show_post(post_id):
    # show the post with the given id, the id is a string
    return f'Post {post_id}, {type(post_id)}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Partie de path {escape(subpath)}'

if __name__ == '__main__':
    app.run()


