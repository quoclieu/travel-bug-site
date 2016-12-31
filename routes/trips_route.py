from flask import render_template, request, session
from travelbug import app
import pyrebase
import json
from process import *
from datetime import datetime as dt

config = {
    "apiKey": "AIzaSyBNT4gDmMljV3Oko-E5WLMnNvW9mBfQ5FE",
    "authDomain": "travel-bugg.firebaseapp.com",
    "databaseURL": "https://travel-bugg.firebaseio.com",
   	"storageBucket": "travel-bugg.appspot.com",
   	"serviceAccount": "serviceAccount"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

@app.route("/trips", methods = ['GET','POST'])
def trips():

	uid = session['uid']

	#checks if user has no trips
	currTrips = db.child("User").child(uid).child("Trip").get().val()
	print(currTrips)
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
			html_str = renderTrips(currTrips)

	
		# PAST TRIPS
		if (pastTrips!=None):
			html_str += "<div id='past-trip-label'>Past Trips</div>"
			html_str += renderTrips(pastTrips)


	html_file = open("templates/_trips.html","w")
	html_file.write(html_str)
	html_file.close()


	############################################################

	title = "My Trips"
	template_vars = {
		"title" : title
	}
	return render_template("trips.html",vars = template_vars, page = "trips")
	

def renderTrips(trips):
	
	
	# to get the dates of all the trips
	# PLS
	# can get trip data here and access 
	trip_date_key = []
	for key in trips: 
		start_date = db.child("Trip").child(key).child("startDate").get().val()
		trip_date_key.append((dt.strptime(start_date, "%d/%m/%Y"),key))
		
	trip_date_key.sort(reverse=True)

	#else display all trips the user is in
	html_str = ""

	#date = start date
	for (date,key) in trip_date_key:
		# all trip details are already pulled
		trip_data = db.child("Trip").child(key).get().val()

		# Get Host Full name
		# PLS
		# can get from trip data no need of another db access
		host = db.child("Trip").child(key).child("User").child("Admin").get().val()
		for host_key in host:
			hostuid = host_key

		host = db.child("User").child(hostuid).child("UserDetails").get().val()
		host = host['firstName']+' '+host['lastName']

		# Get number of travellers
		numtravellers = 1

		#PLS
		# i swear to god i will throw a chair at you if i find out 
		# another unnecessary db access
		travellers = db.child("Trip").child(key).child("User")\
		.child("Regular").get().val()

		if(travellers!=None):
			for traveller in travellers:
				numtravellers+=1

		# Other trip details
		date = getDate(trip_data['startDate'])
		month = getMonth(trip_data['startDate'])
		numDays = trip_data['numberOfDays']
		tripName = trip_data['tripName']
		fulldates = getFullDates(trip_data['startDate'],trip_data['endDate'])
		location = trip_data['location']

		# Need to save key for each trip for fullview
		tripuid = key
	
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
			<div class="title"><a href="{{ url_for('fullview', trip_key="%s", trip_data='%s') }}">%s</a></div>
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

""" % (date,month,numDays,tripuid,json.dumps(trip_data),tripName,fulldates,host,numtravellers,location)
	
	return html_str







