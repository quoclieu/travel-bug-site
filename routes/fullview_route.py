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

	trip_data = db.child("Trip").child(trip_key).get().val()

	trip_days = db.child("Trip").child(trip_key).child("Days").get().val()

	daynum = 0
	html_str = ""

	for day_key in trip_days.values():
		day_data = db.child("DayTrip").child(day_key).get().val()
		
		dayTitle = "IN PROGRESS"
		numAct = 999
		daynum+=1
		date = "IN PROGESS" # should be 19 AUG format

		html_str += """
<div class="day-card">
	<div class="day-label">
		<div class="day-title">
			%s
			<div class="num-act">%s activities planned</div>
		</div>
		<div class="date-circle">
			<div class="daynum">%s</div>
			<div class="date">%s</div>
		</div>
	</div>
""" % (dayTitle,numAct,daynum,date)
		
		if (day_data!=None):
			# Activities
			for act_key in day_data:
				if (day_data!=None):
					for act_key in day_data:
						actName = "IN PROGRESS"
						location = "IN PROGRESS"
						html_str += """
	
	<div class="activity">
		<div class="activity-name">
			%s
			<div class="activity-location">
				<i class="fa fa-map-marker" aria-hidden="true"></i> %s
			</div>
		</div>
		<div class="activity-pic"></div>
	</div>
	<hr>
	


""" % (actName, location)
		html_str+="\n</div>"

	html_file = open("templates/_fullview.html","w")
	html_file.write(html_str)
	html_file.close()

	###############################################################



	title = "Full Trip View"
	template_vars = {
		"title" : title
	}
	return render_template("fullview.html",vars = template_vars)