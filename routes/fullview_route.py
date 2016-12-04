from flask import render_template
from travelbug import app

#server/trips
@app.route("/fullview")
def fullview():
	title = "Full Trip View"
	template_vars = {
		"title" : title
	}
	return render_template("fullview.html",vars = template_vars)