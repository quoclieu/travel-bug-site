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
db = firebase.database()

#server/fullview
@app.route("/fullview")
def fullview():

	
	uid = "wl72WJLpKHYPwQKkOkLzFWsiOEv1"
	trip_key="-KY1wbY8qi-qMzhjApap"

	html_str = ""

	trip_data = db.child("Trip").child(trip_key).get().val()

	trip_days = db.child("Trip").child(trip_key).child("Days").get().val()
	for day_key in trip.values():
		day_data = db.child("DayTrip").child(day_key).get().val()
	
		html += """
<div class="day-card">
	<div class="day-label">
		<div class="day-title">
			Great Ocean Road
			<div class="num-act">8 activities planned</div>
		</div>
		<div class="date-circle">
			<div class="daynum">1</div>
			<div class="date">19 AUG</div>
		</div>
	</div>
"""
		
		for act_key in day_data:
			if (day_data!=None):
				for act_key in day_data:
					html += """




"""









	###############################################################



	title = "Full Trip View"
	template_vars = {
		"title" : title
	}
	return render_template("fullview.html",vars = template_vars)