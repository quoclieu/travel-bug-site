from flask import render_template, session
from travelbug import app

#Front page of our website. Serves as the index, 
#containing links to the other routes/pages

#server/
@app.route("/verify")
def verify():
	title = "Travel Bug"
	template_vars = {
		"title" : title
	}
	
	return render_template("verification.html",vars = template_vars)