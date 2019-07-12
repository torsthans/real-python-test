from flask import Flask

# Create the application object
app = Flask(__name__)


# error handling
app.config["DEBUG"] = True


# use the decorator pattern to
# link the view function to a URL
@app.route("/") # In fact makes a @click.group containg below command?
@app.route("/hello")
def hello_world():
	"""
	define the view using a function, which returns a string
	"""
	return "Hello, World!?!?!?!"


# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query


@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael" :
        return "Hello, {}".format(name)
    else :
        return "Not Found", 404


"""
@app.route("/integer/<int:value>") 
def int_type(value):
    #print(value + 1)
    return "Result = {}".format(value + 1)


@app.route("/float/<float:value>")
def float_type(value):
    #print(value + 1)
    return "Result = {}".format(value + 1)
    
    
# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    #print(value)
    return "Result = {}".format(value)
"""


# start the development server using the run() method
if __name__ == "__main__":
	app.run()
