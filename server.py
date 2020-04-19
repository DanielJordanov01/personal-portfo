from flask import Flask, render_template, request
import csv

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

def save_data_to_csv(data):
	with open('database.csv', 'a+') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar=str(csv.QUOTE_NONE), quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			save_data_to_csv(data)
			return render_template('thankyou.html')
		except:
			return 'Could not send. Check connection'
	else:
		return 'sth went wrong'



if __name__ == '__main__':
	app.run()