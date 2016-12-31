from flask import render_template, session
from travelbug import app

@app.route("/create_trip")
def create_trip():
	title = "New Trip"
	template_vars = {
		"title" : title
	}
	return render_template("create_trip.html",vars = template_vars)
