from flask import render_template
from travelbug import app

#Front page of our website. Serves as the index, 
#containing links to the other routes/pages

#server/
@app.route("/")
def index():
	title = "Travel Bug"
	template_vars = {
		"title" : title
	}
	return render_template("index.html",vars = template_vars)