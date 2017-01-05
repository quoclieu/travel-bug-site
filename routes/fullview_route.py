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

	trip_name = trip_data['tripName']
	
	fulldates = getFullDates(trip_data['startDate'],trip_data['endDate'])

	trip_host = trip_data['User']['Admin']
	 
	for host_key in trip_host:
		host_details = db.child("User").child(host_key).child("UserDetails").get().val()
		host_name = host_details['firstName']+' '+host_details['lastName']
	
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

""" % (trip_name, fulldates, host_name, location)

	trip_days = trip_data['Days']

	html_str+= '<div id="card-grid">'

	for daynum in range(len(trip_days)):

		day = "Day" + str(daynum+1)
		
		day_key = trip_days[day]
		
		full_date = formatFullDate(trip_data['startDate'],daynum)

		date = formatDate(trip_data['startDate'],daynum)

		day_data = db.child("DayTrip").child(day_key).get().val()

		
		day_title = "TEMP"#day_data['dayTitle']
		#has not been implemented on android side yet
		if(day_title == None):
			day_title = "No Title"

########DAYS##########################################
		
		#counts and records number of activities for a specific day
		num_act = 0
		act_time_key = []
		if (day_data!=None):
			for act_key in day_data:
				## Need to refactor this section
				## it counts the number of activities and checks if the activity
				## is a transport
				## If its a transport it skips the count

				act_data = day_data[act_key]
				#what if act_data == None
				#will there ever be a situation when act data == None
				try:
					actName = act_data["eventName"]
				except KeyError:
					continue
				num_act+=1
				act_time_key.append((act_data['timeSort'],act_key,act_data))
			act_time_key.sort()


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
""" % (day_key,(daynum+1),full_date,trip_name,day_title,num_act,(daynum+1),date)
	

########ACTIVITIES################################# 

		if (day_data!=None):
			# Activities
			# dont need the try block because act_time_key 
			# only has activities no transport 
			# so no key error
			for (time,act_key,act_data) in act_time_key:
				if (act_data!=None):
					actName = act_data["eventName"]
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



