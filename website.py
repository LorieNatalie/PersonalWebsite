#website.py

from flask import Flask, render_template

website = Flask(__name__)

@website.route('/')
def home():
    return render_template('index.html')

@website.route('/about')
def about():
    return render_template('about.html')

@website.route('/skills')
def skills():
    return render_template('skills.html')

@website.route('/blog')
def blog():
    return render_template('blog.html')

@website.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    website.run(debug=True)