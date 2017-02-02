from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = 'AIzaSyAbMwmG09ccahMdSZacASf5fb1lHaLs0Iw'

google_places = GooglePlaces(YOUR_API_KEY)

# Grabs an image from a specific location
def getLocImg(location):
    query_result = google_places.text_search(location)

    if query_result.has_attributions:
        print (query_result.html_attributions)

    for place in query_result.places:
        # Returned places from a query are place summaries.
        print (place.name)
        photo = list(place.photos)[0]
        photo.get(maxheight=500, maxwidth=500)
        photo_url = photo.url
    return photo_url