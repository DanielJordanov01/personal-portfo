import smtplib
from email.message import EmailMessage
from keys.keys import password, from_email, personal_email

def send_email(data):
	# email configuration
	email = EmailMessage()
	email['from'] = from_email
	email['to'] = personal_email
	email['subject'] = data['subject']

	# email body
	name = data['name']
	person_email = data['email']
	message = data['message']

	# creating the email body
	email.set_content(f'{name} {person_email} contacted you! \n message: {message}')

	# connecting to server
	with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	    smtp.ehlo()
	    smtp.starttls()
	    smtp.login(from_email, password)
	    smtp.send_message(email)
