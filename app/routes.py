from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'DarkMatter'}
    posts = [
        {
            'author': {'username': 'cartman'},
            'body': 'Suck my balls Kyle!'
        },
        {
            'author': {'username': 'kyle' },
            'body': 'Shutup cartman!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
