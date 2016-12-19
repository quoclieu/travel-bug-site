from flask import render_template, session
from travelbug import app

#login
@app.route("/login")
def login():
	title = "Login"
	template_vars = {
		"title" : title
	}
	return render_template("login.html",vars = template_vars)