from flask import render_template, session, request
from travelbug import app
import pyrebase

config = {
    "apiKey": "AIzaSyBNT4gDmMljV3Oko-E5WLMnNvW9mBfQ5FE",
    "authDomain": "travel-bugg.firebaseapp.com",
    "databaseURL": "https://travel-bugg.firebaseio.com",
   	"storageBucket": "travel-bugg.appspot.com",
   	"serviceAccount": "serviceAccount"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

#server/
@app.route("/verify")
def verify():
	title = "Travel Bug"
	template_vars = {
		"title" : title
	}
	
	uid = session['uid_email_verified']
	db.child('User').child(uid).child('UserDetails').update({"emailVerified": "true"})


	return render_template("verification.html",vars = template_vars)