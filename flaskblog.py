from flask import Flask,render_template,url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '275b8f33ac0f1fdda19e5b9f070c27e9'


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


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form = form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form = form)