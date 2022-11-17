import flask

app = flask.Flask(__name__)

@app.route('/')
def getHomePage():
	return flask.render_template('home.html')

if __name__ == "__main__":
	# app.run() starts the Flask app, you need to call this function to start it.
	# It will most likely by running on http://127.0.0.1:5000/
	app.run()