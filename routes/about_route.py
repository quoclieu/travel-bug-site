from flask import render_template
from travelbug import app

#Page containing information about the team

#server/about-us
@app.route("/about")
def about():
	title = "About Us"
	template_vars = {
		"title" : title
	}
	return render_template("about-us.html",vars = template_vars)