from flask import render_template, request
from travelbug import app
#from firebase import firebase
import pyrebase
import json


config = {
  "apiKey": "AIzaSyBNT4gDmMljV3Oko-E5WLMnNvW9mBfQ5FE",
  "authDomain": "travel-bugg.firebaseapp.com",
  "databaseURL": "https://travel-bugg.firebaseio.com",
  "storageBucket": "travel-bugg.appspot.com",
  "serviceAccount" : "Unknown"

}

firebase = pyrebase.initialize_app(config)
print ("setup complete")

db = firebase.database()

@app.route('/profile', methods = ['POST'])
def profile():	
	#TODO: Refreshing tokens
	auth = firebase.auth()
	user = auth.sign_in_with_email_and_password(request.form["email"], request.form["password"])
	
	return '<h3>' + str(user) + '</h3>'
	


@app.route('/profile1', methods = ['POST'])
def reg():
	auth = firebase.auth()
	#user register in authentication database
	user_data = auth.create_user_with_email_and_password(request.form["email"], request.form["password"])
	
	#have to store user in user database	
	data = {
	    "firstName" : request.form["firstName"],
		"lastName" : request.form["lastName"],
	    "email" : request.form["email"]
	}

	results = db.child("User").child(user_data['localId']).set(data)

	return '<h3>' + str(user_data) + '</h3>'





