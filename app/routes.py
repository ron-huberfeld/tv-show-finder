from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Show Finder')


@app.route('/login')
def login():
    # form = LoginForm()
    return render_template('login.html', title='Sign In')


@app.route('/register')
def register():
    # form = LoginForm()
    return render_template('register.html', title='Sign Up')


@app.route('/password_review')
def password_review():
    return render_template('forgot-password.html', title='Password review')


@app.route('/shows')
def shows():
    return render_template('shows.html', title='Shows')
