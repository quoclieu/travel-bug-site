from flask import Flask, render_template
app = Flask(__name__, static_folder='.', static_url_path='')

#Front page of our website.

#server/
@app.route('/')
def root():
	return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=2526)