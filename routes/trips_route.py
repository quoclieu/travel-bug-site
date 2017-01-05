from flask import render_template, request, session
from travelbug import app
import pyrebase
import json
from process import *
from datetime import datetime as dt
import datetime

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

	
	
	#CURRENT TRIPS
	currTrips = db.child("User").child(uid).child("Trip").get().val()
	if (currTrips!=None):
			html_str = renderTrips(currTrips,uid,"curr")
	
	# PAST TRIPS
	pastTrips = db.child("User").child(uid).child("PastTrip").get().val()
	if (pastTrips!=None):
			html_str += "<div id='past-trip-label'>Past Trips</div>"
			html_str += renderTrips(pastTrips,uid,"past")

    #checks if user has no trips
    #moved around statements to avoid a db access
	if (currTrips == None and pastTrips == None):
		
		html_str = """

<div id="no-trips">
	Looks like you have no plans yet.<br>
	Ready to start planning? Click on add trip!
</div>

"""


	html_file = open("templates/_trips.html","w")
	html_file.write(html_str)
	html_file.close()


	############################################################

	title = "My Trips"
	template_vars = {
		"title" : title
	}
	return render_template("trips.html",vars = template_vars, page = "trips")
	

def renderTrips(trips,uid,type):
	print(dt.now())
	
	#to get the dates of all the trips
	trip_date_key = []
	for key in trips:
		trip_data = db.child("Trip").child(key).get().val() 
		
		#checking for past trips
		#only for curr trips 
		end_date = trip_data['endDate']
		end_date_comp = dt.strptime(end_date, "%d/%m/%Y") + datetime.timedelta(days=1)
		print(end_date_comp)
		
		print(end_date_comp < dt.now())

		if( end_date_comp < dt.now() and type=="curr"):
			print("here") 
			db.child("User").child(uid).child("Trip").child(key).remove()
			db.child("User").child(uid).child("PastTrip").child(key).set("true")
		
		else:
			start_date = trip_data['startDate']
			trip_date_key.append((dt.strptime(start_date, "%d/%m/%Y"),key,trip_data))
		
	if(type=="curr"):
		trip_date_key.sort()
	else: # for past trips the most recent should be the first
		trip_date_key.sort(reverse=True)

	#else display all trips the user is in
	html_str = ""

	#date = start date
	for (date,key,trip_data) in trip_date_key:
		# All trip details are already pulled

	    # Host details
		trip_host = trip_data['User']['Admin']
		
		for host_key in trip_host:
			host_details = db.child("User").child(host_key).child("UserDetails").get().val()
			host_name = host_details['firstName']+' '+host_details['lastName']

		# Get number of travellers
		numtravellers = len(trip_data['User']['Regular']) + 1

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

""" % (date,month,numDays,tripuid,json.dumps(trip_data),tripName,fulldates,host_name,numtravellers,location)
	
	return html_str







