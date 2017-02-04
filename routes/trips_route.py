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

	html_str = ''

	curr_trips_details = None
	past_trips_details = None
	no_curr = False
	no_past = False
	no_trips = False


	#CURRENT TRIPS
	currTrips = db.child("User").child(uid).child("Trip").get().val()
	if (currTrips!=None):
		curr_trips_details = getTripDetails(currTrips,uid,"curr")
		print("curr")
		print(curr_trips_details)

	else:
		no_curr = True
	
	# PAST TRIPS
	pastTrips = db.child("User").child(uid).child("PastTrip").get().val()
	if (pastTrips!=None):
		past_trips_details = getTripDetails(pastTrips,uid,"past")
		print("past")
		print(past_trips_details)

	else:
		no_past = True

    #checks if user has no trips
    #moved around statements to avoid a db access
	if (currTrips == None and pastTrips == None):
		curr_trips_details = None
		past_trips_details = None
		no_trips = True 


	############################################################

	title = "My Trips"
	template_vars = {
		"title" : title
	}
	return render_template("trips.html",vars=template_vars, page="trips", curr_trips=curr_trips_details, past_trips=past_trips_details, no_trips=no_trips, no_curr=no_curr, no_past=no_past)
	

def getTripDetails(trips,uid,type):

	# Trip list contains the key, date and data of the trip 
	# This list is used to sort the trips
	trip_list = []
	for key in trips:
		trip_data = db.child("Trip").child(key).get().val() 
		
		# End date is the last day of the trip 
		# Checking for past trips

		# Converting to date object to compare
		end_date_obj = dt.strptime(trip_data['endDate'], "%d/%m/%Y")

		if( dt.now() > end_date_obj  and type=="curr"):
			
			db.child("User").child(uid).child("Trip").child(key).remove()
			db.child("User").child(uid).child("PastTrip").child(key).set("true")
		
		else:

			start_date_obj = dt.strptime(trip_data['startDate'], "%d/%m/%Y")

			trip_list.append((start_date_obj,key,trip_data))
		
	if(type=="curr"):
		trip_list.sort()

	else: 
		
		# For past trips the most recent should be the first
		
		trip_list.sort(reverse=True)

#########################################################################
	
	# List contains data related to each trip
	# data is in a JSON format
	all_trips = []
	
	for (start_date_obj,trip_key,trip_data) in trip_list:

	    # Host details
		trip_host = trip_data['User']['Admin']
		for host_key in trip_host:
			host_details = db.child("User").child(host_key).child("UserDetails").get().val()
			host_name = host_details['firstName']+' '+host_details['lastName']

		# Regular travellers' details
		regular_travellers = []
	
		for (uid,val) in (trip_data['User']['Regular']).items():
			user_data = db.child("User").child(uid).child("UserDetails").get().val()
			user_name = user_data['firstName']+' '+user_data['lastName']
			regular_travellers.append((user_name,val))

		data = {
			"tripname" : trip_data['tripName'],
			"numtravelers" : len(trip_data['User']['Regular']) + 1,
			"host" : host_name,
			"date" : getDate(trip_data['startDate']),
			"month" : getMonth(trip_data['startDate']),
			"numdays" : trip_data['numberOfDays'],
			"fulldates" :  getFullDates(trip_data['startDate'],trip_data['endDate']),
			"location" : trip_data['location'],
			"tripuid" : trip_key,
			"regular": regular_travellers,
			"dayKeys" : trip_data['Days']

		}

		# Need to save key for each trip for fullview
		all_trips.append(data)

	return all_trips

	#% (date,month,numDays,tripuid,json.dumps(trip_data),tripName,fulldates,host_name,numtravellers,location)
	
	






