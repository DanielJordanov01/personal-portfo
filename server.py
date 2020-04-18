from flask import Flask, render_template, request

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
			print(data)
			return 'sent'
		except:
			return 'Could not send. Check connection'
	else:
		return 'sth went wrong'

if __name__ == '__main__':
	app.run()