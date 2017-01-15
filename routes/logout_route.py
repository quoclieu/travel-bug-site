from flask import render_template, session, redirect
from travelbug import app

@app.route("/logout")
def logout():
	session.pop('uid', None)
	session.pop('logged_in', None)

	return redirect('/login')
