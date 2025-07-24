#website.py

from flask import Flask, render_template

website = Flask(__name__)

@website.route('/')
def home():
    return render_template('index.html')

@website.route('/projects')
def projects():
    return render_template('projects.html')

@website.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    website.run(debug=True)