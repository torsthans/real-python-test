from flask import Flask

# Create the application object
app = Flask(__name__)

# use the decorator pattern to
# link the view function to a URL
@app.route("/")
@app.route("/hello")

def hello_world():
	"""
	define the view using a function, which returns a string
	"""
	return "Hello, World"

# start the development server using the run() method
if __name__ == "__main__":
	app.run()
