from flask import render_template
from travelbug import app


@app.route("/register")
def register():
	title = "Register"
	template_vars = {
		"title" : title
	}
	return render_template("register.html",vars = template_vars)