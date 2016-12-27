from flask import render_template, session
from travelbug import app

#server/about
@app.route("/about")
def about():
	title = "About"
	template_vars = {
		"title" : title
	}
	return render_template("about.html",vars = template_vars)