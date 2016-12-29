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


#server/day
@app.route("/day")
def day():
	uid = session['uid']

	day_key = request.args.get('day_key', None)
	trip_key = request.args.get('trip_key', None)

	day_data = db.child("DayTrip").child(day_key).get().val()
	trip_data = db.child("Trip").child(trip_key).get().val()


	dayNum = '1'
	date = '20 August 2016' 
	tripName = 'yeti'
	dayName = 'TEMP'

	html_str = '''
	<div id="dropdown">
		<div class="day-num">%s</div>
		<div class="date">
			%s
			<i class="fa fa-angle-double-down" aria-hidden="true"></i>
		</div>
	</div>
	

	<div class="trip-name">%s</div>
	<div class="day-name">%s</div>

	<div id="schedule-block">
		<div id="schedule-container">

	''' %(dayNum, date, tripName,dayName)

	# Sorts list of time
	time_list = []
	for act_key in day_data:
		act_data = db.child("DayTrip").child(day_key).child(act_key).get().val()
		time_list.append(act_data['timeSort'])

	time_list = sorted(time_list)

	# Prints activities and transport in accordance to the sorted time list
	for time in time_list:
		for act_key in day_data:
			act_data = db.child("DayTrip").child(day_key).child(act_key).get().val()
			if(time == act_data['timeSort']):
		
				try:
					# Handles printing the transport slot
					transport = act_data['transport']

					time = getTime(int(act_data['timeSort']))
					transport_icon = getIcon(transport)
					description = act_data['description']

					html_str += '''

			<div class="transport-block">
				<div class="col span_10" style="font-size:10px;font-weight:500;padding-top:16px;">
					%s
				</div>

				<div class="transport col span_20"><i class="fa %s" aria-hidden="true"></i>
					<span class ="boxed">%s</span>
				</div>
			</div>
			<div style="clear:both;"></div>
		'''	% (time,transport_icon,description)

				except KeyError:
					# Handles printing activities

					time = getTime(int(act_data['timeSort']))
					title = act_data['eventName']
					location = act_data['location']['address']
					description = act_data['description']

					html_str += '''
	<div class="activity section group">
			<div class="col span_10" style="font-size:10px;font-weight:500;padding-top:55px;">
				%s
			</div>

			<div class="circle pic col span_20"></div>
		
			<div class="text-block col span_60">
				<span style="font-weight:500;">%s</span>
				<div class="location">
					<i class="fa fa-map-marker" aria-hidden="true"></i> <i>%s</i>
				</div>
				<div class="description">
					%s
				</div>
				<div class="ratings"></div>
			</div>
		</div>
	<div style="clear:both;"></div>
''' % (time, title, location, description)

	html_str += '''
		</div>
	</div>
	'''

	html_file = open("templates/_day_schedule.html","w")
	html_file.write(html_str)
	html_file.close()

	###################################################################
	title = "Day"
	template_vars = {
		"title" : title
	}
	return render_template("day.html",vars = template_vars)