# Instructions

1. GCP API Configuration

In order to access Google sheets we need to connect through Google Sheets API. For that we need to follow these steps:

a. login to GCP Console.

b. Create Project

c. Go to API Services and search Google Drive API. Enable it.

d. Similarly search Google sheets API and enable it. 

e. Goto Credentials and create client_secret.json file 

f. Copy this file to project folder

2. Create Project on Heroku and Clone to local machine 

Install the Heroku CLI
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.


`$ heroku login`

Clone the repository
Use Git to clone PROJECT_NAME's source code to your local machine.
```
$ heroku git:clone -a PROJECT_NAME`
$ cd PROJECT_NAME
```

Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.
```
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```

The application is now deployed. Ensure that at least one instance of the app is running:

`heroku ps:scale web=1`

Now run

`heroku open`
