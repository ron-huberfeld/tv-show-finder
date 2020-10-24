from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
import requests


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.j2', title='Show Finder')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('{} is logged in'.format(form.email.data))
        return redirect(url_for('shows'))
    return render_template('login.j2', title='Sign In', form=form)


@app.route('/register')
def register():
    return render_template('register.j2', title='Sign Up')


@app.route('/password_review')
def password_review():
    return render_template('forgot-password.j2', title='Password review')


@app.route('/shows')
def shows():
    response = requests.get('http://api.tvmaze.com/shows').json()
    return render_template('shows.j2', title='Shows', shows=response)
