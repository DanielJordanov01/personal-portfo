from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('about.html')

@app.route('/experience')
def experience():
	return render_template('experience.html')

@app.route('/education')
def education():
	return render_template('education.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')