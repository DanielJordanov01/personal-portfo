import csv

def save_data_to_csv(data):
	with open('database.csv', 'a+') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar=str(csv.QUOTE_NONE), quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])