from flask import Flask, render_template
# from gevent.wsgi import WSGIServer
app = Flask(__name__, static_folder='.', static_url_path='')

#import all routes from routes directory
from routes import *

if __name__ == "__main__":
    app.run(debug=True, port=2526)
	# http_server = WSGIServer(('', 2526), app)
	# http_server.serve_forever()
