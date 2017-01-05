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
	#PLS
	#i dont think we need trip key

	#PLS
	#We dont really need trip data 
	#day data can be passed through url  
	day_data = db.child("DayTrip").child(day_key).get().val()

	dayNum = request.args.get('daynum', None)

	date = request.args.get('date', None)
	trip_name = request.args.get('trip_name', None)
	day_name = 'TEMP'


	html_str = '''
	<div id="dropdown">
		<div class="day-num">%s</div>
		<div class="date">
			%s
		</div>
	</div>
	

	<div class="trip-name">%s</div>
	<div class="day-name">%s</div>

	<div id="schedule-block">
		<div id="schedule-container">

	''' %(dayNum,date,trip_name,day_name)

	
	# Sorts list of time
	act_time_key = []
	for act_key in day_data:
		act_data = db.child("DayTrip").child(day_key).child(act_key).get().val()
		act_time_key.append((act_data['time'],act_key,act_data))
	act_time_key.sort()

	# Prints activities and transport in accordance to the sorted time list
	for (time,act_key,act_data) in act_time_key:
		try:
			# Handles printing the transport slot
			transport = act_data['transport']
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
			title = act_data['eventName']
			location = act_data['location']['address']
			description = act_data['description']

			#Ratings and Comments
			numUp =  0
			numDown = 0
			
			#Checks if votes section exist
			try:
				votes = act_data['Votes']

				for (uid,val) in votes.items():
					if (val == "true"):
						numUp+=1
					if (val == "false"):
						numDown+=1
			except KeyError:
				pass

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
				<div class="ratings right">
					%s<i class="fa fa-thumbs-up" aria-hidden="true"></i>
					%s<i class="fa fa-thumbs-down" aria-hidden="true"></i>
					<i class="fa fa-comment" aria-hidden="true"></i>
				</div>
			</div>
		</div>
	<div style="clear:both;"></div>
''' % (time, title, location, description, numUp, numDown)

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


