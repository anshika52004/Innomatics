from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import string
import random
import validators

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SECRET_KEY'] = 'secret-key'
db = SQLAlchemy(app)

# Database Model
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(10), nullable=False, unique=True)

# Generate short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None

    if request.method == 'POST':
        original_url = request.form['original_url']

        # Validate URL
        if not validators.url(original_url):
            flash('Invalid URL. Please enter a valid URL.', 'danger')
            return redirect(url_for('index'))

        short_code = generate_short_url()

        new_url = URL(
            original_url=original_url,
            short_url=short_code
        )

        db.session.add(new_url)
        db.session.commit()

        short_url = request.host_url + short_code

    return render_template('index.html', short_url=short_url)

@app.route('/history')
def history():
    urls = URL.query.all()
    return render_template('history.html', urls=urls)

@app.route('/<short_code>')
def redirect_url(short_code):
    url = URL.query.filter_by(short_url=short_code).first_or_404()
    return redirect(url.original_url)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
