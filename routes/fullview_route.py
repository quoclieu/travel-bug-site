from flask import render_template
from travelbug import app
import pyrebase
from process import *

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

	
	uid = "7HYXTyUfgMhXVpF1ucU7zgjush52"
	trip_key="-KY1wbY8qi-qMzhjApap"


	##### REVAMP THIS ENTIRE SECTION - TRANSFER DATA AS A DICT FROM PREV PAGE INTO HERE##
	trip_data = db.child("Trip").child(trip_key).get().val()
	user_data = db.child("User").child(uid).get().val()


	tripName = trip_data['tripName']
	fulldates = getFullDates(trip_data['startDate'],trip_data['endDate'])
	# Get Host Full name
	host = db.child("Trip").child(trip_key).child("User").child("Admin").get().val()
	for host_key in host:
		hostuid = host_key

	host = db.child("User").child(hostuid).child("UserDetails").get().val()
	host = host['firstName']+' '+host['lastName']
	
	location = trip_data['location']


	######################################################################################

	html_str = """

<div class="trip-details">
	%s<br>
	<span style="color:#9F9F9F">%s</span>
	<div class="host">Hosted by %s</div>
	<hr>
	<div class="location">
		<i class="fa fa-map-marker" aria-hidden="true"></i> %s
	</div>
</div>

""" % (tripName, fulldates, host, location)



	trip_data = db.child("Trip").child(trip_key).get().val()

	trip_days = db.child("Trip").child(trip_key).child("Days").get().val()

	daynum = 0

	html_str+= '<div id="card-grid">'

	for day_key in trip_days.values():
		day_data = db.child("DayTrip").child(day_key).get().val()

		dayTitle = "TEMP"#day_data[dayTitle]


########DAYS##########################################
		
		#counts and records number of activities for a specific day
		numAct = 0
		if (day_data!=None):
			for act_key in day_data:
				numAct+=1

		if(dayTitle == None):
			dayTitle = "No Title"

		date = formatDate(trip_data['startDate'],daynum) # should be 19 AUG format
		daynum+=1
		

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

########ACTIVITIES################################# 

		if (day_data!=None):
			# Activities
			for act_key in day_data:
				act_data = db.child("DayTrip").child(day_key).child(act_key).get().val()
				if (act_data!=None):
					actName = "yes"#act_data["eventName"]
					location = "yes"#act_data["location"]["address"]
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



