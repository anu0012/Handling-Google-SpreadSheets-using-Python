import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, url_for, render_template, request, redirect, session
import json

app = Flask(__name__)

@app.route('/')
def home():
	# use creds to create a client to interact with the Google Drive API
	scope = ['https://spreadsheets.google.com/feeds',
	         'https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)

	# Find a workbook by name and open the first sheet
	# Make sure you use the right name here.
	sheet = client.open("Copy of Sample Pair Sheet").sheet1
	list_of_rows = sheet.get_all_values()

	responses = ['Almost always available', 'Sometimes available', 'Never available',
	 'Not a specific product', 'Not Sure/Can\'t Determine']
	data = json.dumps(list_of_rows)
	loaded_data = json.loads(data)
	return render_template('index.html', data=list_of_rows, responses=responses)

@app.route('/parse_data', methods=['POST'])
def parse_data():
    if request.method == "POST":
    	data = request.get_json()
    	print(data['answers'])
    	return 'Success'

if __name__ == '__main__':
    app.run()
