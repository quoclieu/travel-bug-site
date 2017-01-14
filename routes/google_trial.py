from googleplaces import GooglePlaces, types, lang
from flask import render_template, request, session
from travelbug import app

@app.route('/google_API')
def google_API():
	apiKey = "AIzaSyAbMwmG09ccahMdSZacASf5fb1lHaLs0Iw"
	google_places = GooglePlaces(apiKey)
	query_result = google_places.nearby_search(
        location='London, England', keyword='Fish and Chips',
        radius=2000, types=[types.TYPE_FOOD])

	if query_result.has_attributions:
		print(query_result.html_attributions)

    # Returned places from a query are place summaries.
	place = query_result.places[0]
	print(place.name)
    

	html_str = ""

	i = 0

	for photo in place.photos:
		if(i == 0):
	    	# 'maxheight' or 'maxwidth' is required
			photo.get(maxheight=500, maxwidth=500)

	   		 # MIME-type, e.g. 'image/jpeg'
		

			html_str += ''' 
			<img src = %s height = %d width = %d>
	    	 
			''' % (photo.url, 500, 500)

			i += 1
		else: 
			break

	html_file = open("templates/_google_trial.html","w")
	html_file.write(html_str)
	html_file.close()
    

	title = "Google API"
	template_vars = {
		"title" : title
	}
	return render_template("_google_trial.html",vars = template_vars)



