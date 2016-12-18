from flask import render_template
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


#server/fullview
@app.route("/fullview")
def fullview():

	db = firebase.database()
	uid = "wl72WJLpKHYPwQKkOkLzFWsiOEv1"

	
	html_str = ""

















	###############################################################



	title = "Full Trip View"
	template_vars = {
		"title" : title
	}
	return render_template("fullview.html",vars = template_vars)