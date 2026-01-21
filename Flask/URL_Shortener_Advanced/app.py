from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import validators
import random
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secretkey'
db = SQLAlchemy(app)

# ------------------ DATABASE MODELS ------------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(9), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(6), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# ------------------ UTILS ------------------

def generate_short_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

# ------------------ ROUTES ------------------

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        flash("Invalid username or password", "danger")
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if len(username) < 5 or len(username) > 9:
            flash("Username must be between 5 to 9 characters long", "danger")
            return redirect(url_for('signup'))

        if User.query.filter_by(username=username).first():
            flash("This username already exists...", "danger")
            return redirect(url_for('signup'))

        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash("Signup successful! Please login.", "success")
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    short_url = None
    if request.method == 'POST':
        original_url = request.form['original_url']

        if not validators.url(original_url):
            flash("Invalid URL", "danger")
            return redirect(url_for('dashboard'))

        code = generate_short_code()
        new_url = URL(
            original_url=original_url,
            short_code=code,
            user_id=session['user_id']
        )
        db.session.add(new_url)
        db.session.commit()
        short_url = request.host_url + code

    urls = URL.query.filter_by(user_id=session['user_id']).all()
    return render_template('dashboard.html', short_url=short_url, urls=urls)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/<code>')
def redirect_url(code):
    url = URL.query.filter_by(short_code=code).first_or_404()
    return redirect(url.original_url)

# ------------------ RUN ------------------

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
