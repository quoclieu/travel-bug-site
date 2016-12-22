from flask import render_template, session, redirect, request
from travelbug import app
import pyrebase
from register_form import RegisterForm

config = {
    "apiKey": "AIzaSyBNT4gDmMljV3Oko-E5WLMnNvW9mBfQ5FE",
    "authDomain": "travel-bugg.firebaseapp.com",
    "databaseURL": "https://travel-bugg.firebaseio.com",
   	"storageBucket": "travel-bugg.appspot.com",
   	"serviceAccount": "serviceAccount"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

#login
@app.route("/register", methods=['GET', 'POST'])
def register():
	title = "Register"
	template_vars = {
		"title" : title
	}

	form = RegisterForm()

	if form.validate_on_submit():
		
		auth = firebase.auth()
		#user register in authentication database
		
		try:
			user_data = auth.create_user_with_email_and_password(request.form["email"], request.form["password"])
		except:
			return render_template("register.html",vars = template_vars, form=form, is_error=True)
	
		#have to store user in user database	
		data = {
	    	"firstName" : request.form["firstname"],
			"lastName" : request.form["lastname"],
	    	"email" : request.form["email"]
		}

		db.child("User").child(user_data['localId']).set(data)

		session['uid'] = user_data['localId']

		return redirect('/trips')
	return render_template("register.html",vars = template_vars, form=form, is_error=False)