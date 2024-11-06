# Section 1 Flask Jinja Handout
# You don't always have to respond to HTTP requests with plain text. You can choose to respond to them with HTML. 
# While we can output a string of HTML, it is better practice to output a separate HTML file. Colt will walk you through this. 

# Section 2 Introduction to Templates
# Goals
    # Explain what HTML templates are, and why they are useful
    # Use Jinja to create HTML templates for our Flask applications
    # Debug our Flask applications more quickly by installing the Flask Debug Toolbar
    # Serve static files (CSS, JS, etc) with Flask

# Review
# Views
# Views are functions that return a string (a string of HTML)

# Routes
# Routes define the URL that will run a view function.
# They are declared by using decorators.
# A route and view function:

# @app.route('/form')
# def show_form():
#     """Show greeting form."""

#     return """
#       <!DOCTYPE html>
#       <html>
#         <head>
#           <title>Hi There!</title>
#         </head>
#         <body>
#           <h1>Hi There!</h1>
#           <form action="/greet">
#             What's your name? <input name="person">
#             <button>Go!</button>
#           </form>
#         </body>
#       </html>
#     """
# This is kind of messy to read through (and we don’t get nice things like color-highlighting in editors). 
# Much better to keep HTML in a separate file.

# Templates
# How Can Templates Help?
    # Produce HTML
    # Allows your responses to be dynamically created
        # Can use variables passed from your views
        # For loops, if/else statements
    # Can inherit from other templates to minimize repetition

# Jinja
# Jinja is a popular template system for Python, used by Flask.
# There are many template systems for Python. Jinja is a particularly popular one. 
# Django has its own template system, which served as an inspiration for Jinja.

# Templates Directory
# Your templates directory lives under your project directory. Flask knows to look for them there.

# my-project-directory/
#   venv/
#   app.py
#   templates/
#     hello.html

# Section 3 Debug Toolbar
# Flask Debug Toolbar
# Ultra-useful add-on for Flask that shows, in browser, details about app.
    
# Install add-on product:
# (venv) $ pip3 install flask-debugtoolbar

# Add the following to your Flask app.py:

# from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension

# app = Flask(__name__)
# app.config['SECRET_KEY'] = "oh-so-secret"
# debug = DebugToolbarExtension(app)
# ... # rest of file continues

# SECRET_KEY
# For now, that secret key doesn’t really have to be something secret (it’s fine to check this file into your GitHub, and you can use any string for the SECRET_KEY.
# Later, when we talk about security & deployment, we’ll talk about when and how to actually keep this secret.

# Using The Toolbar
    # Request Vars
        # Explore what Flask got in request from browser
    # HTTP Headers
        # Can be useful to explore all headers your browser sent
    # Templates
        # What templates were used, and what was passed to them?
    # Route List
        # What are all routes your app defines?