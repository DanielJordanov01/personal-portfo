from flask import Flask, render_template, request
from packages.database.save_data import save_data_to_csv
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

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			save_data_to_csv(data)
			return render_template('thankyou.html')
		except:
			return render_template('error.html')


if __name__ == '__main__':
	app.run()