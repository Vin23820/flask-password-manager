from flask import Flask, render_template, redirect, url_for, request, flash
from models import db, User, PasswordEntry
from utils import hash_password, verify_password
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = hash_password(request.form["password"])

        if User.query.filter_by(username=username).first():
            flash("Username already exists")
            return redirect(url_for("register"))

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful. Please login.")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and verify_password(user.password, password):
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials")

    return render_template("login.html")

@app.route("/dashboard")
@login_required
def dashboard():
    entries = PasswordEntry.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", entries=entries)

@app.route("/add", methods=["GET", "POST"])
@login_required
def add_password():
    if request.method == "POST":
        website = request.form["website"]
        email = request.form["email"]
        password = request.form["password"]

        entry = PasswordEntry(
            website=website,
            email=email,
            password=password,
            user_id=current_user.id
        )
        db.session.add(entry)
        db.session.commit()
        flash("Password saved successfully")
        return redirect(url_for("dashboard"))

    return render_template("add_password.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug=True)

