import csv

def save_data_to_csv(data):
	with open('database.csv', 'a+') as database:
		name = data['name']
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database, delimiter=',', quotechar=str(csv.QUOTE_NONE), quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,email,subject,message])