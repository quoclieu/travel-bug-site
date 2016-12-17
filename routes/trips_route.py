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

#Trip page

#server/mytrips
@app.route("/trips")
def trips():

	db = firebase.database()
	uid = "Bm1ICRoTU2TmEZj73dLt3QCg0sD2"

	trips = db.child("User").child(uid).child("Trip").get().val()

	if (trips == None):
		#if user has no trips
		html_str = """

<div id="no-trips">
	Looks like you have no plans yet.<br>
	Ready to start planning? Click on add trip!
</div>

"""

	else:
		#else display all trips the user is in
		html_str = ""

		for key in trips:
			trip_data = db.child("Trip").child(key).get().val()

			date = "19"
			month = "Jan"
			numDays = trip_data['numberOfDays']
			tripName = trip_data['tripName']
			fulldates = "19-27 August"
			host = "Jason"
			numtravellers = "2"
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

	html_file = open("templates/_trips.html","w")
	html_file.write(html_str)
	html_file.close()





	############################################################

	title = "My Trips"
	template_vars = {
		"title" : title
	}
	return render_template("trips.html",vars = template_vars)

