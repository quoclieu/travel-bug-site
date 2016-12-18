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

#server/mytrips
@app.route("/trips")
def trips():

	db = firebase.database()
	uid = "wl72WJLpKHYPwQKkOkLzFWsiOEv1"

	#checks if user has no trips
	currTrips = db.child("User").child(uid).child("Trip").get().val()
	pastTrips = db.child("User").child(uid).child("PastTrip").get().val()
	if (currTrips == None and pastTrips == None):
		
		html_str = """

<div id="no-trips">
	Looks like you have no plans yet.<br>
	Ready to start planning? Click on add trip!
</div>

"""

	else:
		#CURRENT TRIPS
		if (currTrips!=None):
			html_str = renderTrips("Trip",db,uid)

	
		# PAST TRIPS
		if (pastTrips!=None):
			html_str += "<div id='past-trip-label'>Past Trips</div>"
			html_str += renderTrips("PastTrip",db,uid)


	html_file = open("templates/_trips.html","w")
	html_file.write(html_str)
	html_file.close()


	############################################################

	title = "My Trips"
	template_vars = {
		"title" : title
	}
	return render_template("trips.html",vars = template_vars)




def renderTrips(trip_label,database,uid):
	db = database
	trips = db.child("User").child(uid).child(trip_label).get().val()
	

	#else display all trips the user is in
	html_str = ""

	for key in trips:
		trip_data = db.child("Trip").child(key).get().val()

		# Get Host Full name
		host = db.child("Trip").child(key).child("User").child("Admin").get().val()
		for host_key in host:
			hostuid = host_key

		host = db.child("User").child(hostuid).child("UserDetails").get().val()
		host = host['firstName']+' '+host['lastName']

		# Get number of travellers
		numtravellers = 1

		travellers = db.child("Trip").child(key).child("User")\
		.child("Regular").get().val()

		if(travellers!=None):
			for traveller in travellers:
				numtravellers+=1

		#Other trip details
		date = getDate(trip_data['startDate'])
		month = getMonth(trip_data['startDate'])
		numDays = trip_data['numberOfDays']
		tripName = trip_data['tripName']
		fulldates = getFullDates(trip_data['startDate'],trip_data['endDate'])
		location = trip_data['location']

		html_str += """

<div class="card-block">
<div class="date-box">
	<div class="date">%s</div>
	<div class="month">%s</div>
</div>

<div class="card-left"></div>

<div class="card-right">
	<div class="trip-textbox">
		<div class="days">%s DAYS</div>
		<div class="title">%s</div>
		<div class="full-dates">%s</div>
		<div class="host">Hosted by %s</div>
		<hr/>
		<div class="numtravelers">%s travelers</div>

		<div class="location">
			<i class="fa fa-map-marker" aria-hidden="true"></i> %s
		</div>
	</div>
</div>

</div>

""" % (date,month,numDays,tripName,fulldates,host,numtravellers,location)
	
	return html_str







