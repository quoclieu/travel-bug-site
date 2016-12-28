from flask import render_template, session
from travelbug import app

@app.route("/contact")
def contact():
	title = "Contact"
	template_vars = {
		"title" : title
	}
	return render_template("contact.html",vars = template_vars)
