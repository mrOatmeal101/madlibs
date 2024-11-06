from flask import Flask, request, render_template

app = Flask(__name__)

# showing how to use a template html file to make a page. 
@app.route('/')
def home_page():
    return render_template('hello.html')

# showing that you can have multipule routes leading to the same html file. 
@app.route('/hello')
def say_hello():
    return render_template('hello.html')

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

