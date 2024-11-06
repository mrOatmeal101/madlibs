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