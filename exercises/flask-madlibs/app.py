# 1st step was to setup Virtual Enviornment inside the flask-madlibs folder to keep a clean work environment. 
# then I installed the requirements.txt that was provided so that all of the individual packages where installed.
# next i updated the git.ignore file so that the venv would not be added to my local git.
# followed by creating the app.py file with: touch app.py

# first line of code is to import Flask from the module flask 
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story



# to create the flask application or instantiate it with app = Flask(__name__)
# this is a class and it makes us an app object.
# we store it in a variable called app.
app = Flask(__name__)
app.config['SECRET_KEY'] = "frejyathecat"
debug = DebugToolbarExtension(app)
# then in the command line: flask run
# The server is now running and use ctrl + c to quit.
# if the file was called my_app.py, you would need to run the command, while in the VE:
    # FLASK_AAP=my_app.py flask run
# Set export FLASK EVN=development in my bash profile. 
# Also installed the debugger under the requirements.

# after testing server, set up templates folder and begin adding html pages.
# Started with hello.html for the the first route to the home page.\
# also imported the render_template from flask
@app.route('/')
def home_page():
    # used the function render template and give it the name of html file to render. 
    return render_template('hello.html')

# adding route to the madlib form page for user input
@app.route('/madlibform')
def madlib_form_page():
    return render_template('madlibform.html')

# # making an output page for when the form from madlibform sends a request to here.
@app.route('/story')
def madlib_story():
    place = request.args['place']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    pural_noun = request.args['pural_noun']
    return render_template('story.html', place=place, noun=noun, verb=verb, adjective=adjective, pural_noun=pural_noun)

# @app.route("/")
# def ask_questions():
#     """Generate and show form to ask words."""

#     prompts = story.prompts

#     return render_template("hello.html"), prompts=prompts)

# @app.route("/story")
# def show_story():
#     """Show story result."""

#     text = story.generate(request.args)

#     return render_template("story.html"), text=text)