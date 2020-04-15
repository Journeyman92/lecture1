#!/usr/bin/python3
import os
from flask import Flask, session, render_template, flash, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '3e3e0c9b2da5b19bf2b80a1506ddc92d'

app.static_folder = 'static'
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/Home")
def index():
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])

def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        flash(f"Account created for {form.username.data}!",category='success' )

        return redirect({{ url_for('index') }})

    return render_template('register.html',title='Register',form=form)


@app.route('/login',methods=['POST','GET'])

def login():

    form = LoginForm()

    if form.validate_on_submit():

        flash(f'Account created for {form.username.data}!','sucess')

    return render_template('login.html',title='Login',form=form)


@app.route('/contact')

def contact():
    return render_template('contact.html')

@app.route('/about')

def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

