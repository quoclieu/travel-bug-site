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

	# trip_vars = {
	# 	"date" : date,
	# 	"month" : month,
	# 	"title" : title,
	# 	"days" : days,
	# 	"full-dates" : fulldates,
	# 	"host" : host,
	# 	"numtravellers" : numtravellers,
	# 	"location" : location
	# }
	return render_template("trips.html",vars = template_vars)