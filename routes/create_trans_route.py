from flask import render_template, session, redirect, request, url_for
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



@app.route('/create_trans', methods=['GET', 'POST'])
def create_trans():

	print(request.form["transport"])
	print(request.form["time"])
	print(request.form["description"])
	day_key = request.form.get("day_key","")
	print(request.form.get("daynum",""))

	#return str("hi")

	trans_data = {
	    "time" : request.form["time"],
	    "description" : request.form["description"],
	    "transport" : request.form["transport"]


	}

	db.child("DayTrip").child(day_key).push(trans_data)

	return redirect(url_for("day", day_key=request.form.get("day_key",""), daynum=request.form.get("daynum",""), date=request.form.get("date",""), trip_name=request.form.get("trip_name","") ) )
	