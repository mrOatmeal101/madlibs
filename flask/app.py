from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "frejyathecat"
debug = DebugToolbarExtension(app)

# showing how to use a template html file to make a page. 
@app.route('/')
def home_page():
    return render_template('hello.html')

# showing that you can have multipule routes leading to the same html file. 
@app.route('/hello/<name>')
def say_hello(name):
    return render_template('hello.html') # http://127.0.0.1:5000/hello/stacy
# under the Request Vars you will see:
# View Function	kwargs
# app.say_hello	name=stacy

# POSTS = {
#     1: "I like kitties",
#     2: "i like dogs",
#     3: "double rainbow all the way",
#     4: "orange amps"
# }

# @app.route('/posts/<int:id>') 
# def find_posts(id):
#     post = POSTS.get(id, "Post Not Found")
#     return f"<p>{post}</p>"

