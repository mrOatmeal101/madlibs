from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint

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

# how to make a random number show up on your web page. 
@app.route('/lucky')
def lucky_number():
    num = randint(1,20)
    return render_template('lucky.html', lucky_num=num, msg="you are so lucky")
# got this output first: Your lucky number is: 20

@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/greet')
def get_greeting():
    username = request.args['username']
    return render_template('greet.html', username=username)

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

