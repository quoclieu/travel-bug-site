from flask import render_template, request, session
from travelbug import app
import pyrebase
import json
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

	
	uid = session['uid']
	trip_key=request.args.get('trip_key', None)

	#TODO - TRANSFER DATA AS A DICT FROM PREV PAGE INTO HERE
	#done!
	trip_data =json.loads(request.args.get('trip_data'))
	print(trip_data)
	#PLS
	#we do not need user data

	tripName = trip_data['tripName']
	fulldates = getFullDates(trip_data['startDate'],trip_data['endDate'])

	# Get Host Full name
	#PLS
	# -.- another unnecessary db access
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
	<hr align="left">
	<div class="location">
		<i class="fa fa-map-marker" aria-hidden="true"></i> %s
	</div>
</div>

""" % (tripName, fulldates, host, location)

	#PLS
	#trip data pulled twice
	trip_data = db.child("Trip").child(trip_key).get().val()

	#PLS
	#can get from previously pulled trip data
	trip_days = db.child("Trip").child(trip_key).child("Days").get().val()

	html_str+= '<div id="card-grid">'

	for daynum in range(len(trip_days)):
		day = "Day" + str(daynum+1)
		#PLS
		#can get from previously pulled trip data
		day_key = db.child("Trip").child(trip_key).child("Days").child(day).get().val()

		#this is necessary
		day_data = db.child("DayTrip").child(day_key).get().val()

		dayTitle = "TEMP"#day_data[dayTitle]
		#has not been implemented on android side yet

########DAYS##########################################
		
		#counts and records number of activities for a specific day
		numAct = 0
		act_time_key = []
		if (day_data!=None):
			for act_key in day_data:
				## Need to refactor this section
				## it counts the number of activities and checks if the activity
				## is a transport
				## If its a transport it skips the count
				#PLS
				#can get from previously pulled day data
				act_data = db.child("DayTrip").child(day_key).child(act_key).get().val()
				try:
					actName = act_data["eventName"]
				except KeyError:
					continue
				numAct+=1
				act_time_key.append((act_data['time'],act_key))
			act_time_key.sort()
			




		if(dayTitle == None):
			dayTitle = "No Title"

		date = formatDate(trip_data['startDate'],daynum)
		
		

		html_str += """
<div class="day-card">
	<div class="day-label">
		<div class="day-title">
			<a href="{{ url_for('day', day_key='%s', daynum=%d, date="%s", trip_name='%s') }}">%s</a>
			<div class="num-act">%s activities planned</div>
		</div>
		<div class="date-circle">
			<div class="daynum">%s</div>
			<div class="date">%s</div>
		</div>
	</div>
	<hr>
""" % (day_key,(daynum+1),date,trip_data['tripName'],dayTitle,numAct,(daynum+1),date)
		print("fullview")
		print(trip_data['tripName'])

########ACTIVITIES################################# 

		if (day_data!=None):
			# Activities
			for (time,act_key) in act_time_key:
				#PLS
				# act_data can be outside the for loop 
				act_data = db.child("DayTrip").child(day_key).child(act_key).get().val()
				if (act_data!=None):
					try:
						actName = act_data["eventName"]
					except KeyError:
						continue
					location = act_data["location"]["address"]
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



