from flask import render_template, flash, redirect,url_for
from flaskblog.models import User,Post
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app,db,bcrypt


posts= [
    {
        'author':'Author 1',
        'title':'Blog Post 1',
        'content':'content',
        'date_posted':'April 20, 2018'
    },
    {
        'author':'Author 1',
        'title':'Blog Post 1',
        'content':'content',
        'date_posted':'April 20, 2018'
    }
]


@app.route("/")
def home(): 
    return render_template("home.html",title="homepage", posts=posts)


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account Created Successfully You can Now LogIn", 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form = form)


@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "hadi@hadi.com" and form.password.data == "hadi":
            flash("Login Successfull", category="success")
            redirect(url_for('home'))

        else:
            flash("Credentials Incorrect", category="danger")

    return render_template("login.html", title="Login", form = form)