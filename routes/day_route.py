from flask import render_template, session
from travelbug import app

#Trip page

#server/mytrips
@app.route("/day")
def day():


















	###################################################################
	title = "Day"
	template_vars = {
		"title" : title
	}
	return render_template("day.html",vars = template_vars)