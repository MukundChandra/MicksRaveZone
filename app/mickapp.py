import flask

app = flask.Flask(__name__,static_url_path='/static')

@app.route('/')
def getHomePage():
	return flask.render_template('home.html')

@app.route('/myprojects')
def getProjectsPage():
	return flask.render_template('myprojects.html')

@app.route('/myprojects/<projectname>')
def getProjectToRender(projectname):
	# Can add some verification about the app being present in the server or not, and route them accordingly to the page.
	return flask.render_template('projectshowcase.html',projectname=projectname)

@app.route('/signin')
def getSignInPage():
	return flask.render_template('signin.html')

if __name__ == "__main__":
	# app.run() starts the Flask app, you need to call this function to start it.
	# It will most likely by running on http://127.0.0.1:5000/
	app.run(host="0.0.0.0",port=80)