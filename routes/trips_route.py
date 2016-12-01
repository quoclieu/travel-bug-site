from flask import render_template
from travelbug import app

#Trip page

#server/mytrips
@app.route("/trips")
def trips():
	title = "My Trips"
	template_vars = {
		"title" : title
	}
	return render_template("trip.html",vars = template_vars)