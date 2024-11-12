from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

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

@app.route('/luckytwo')
def lucky_numbertwo():
    num = randint(1,10)
    return render_template('lucky.html', lucky_num=num, msg="you are so lucky")
# got this output first: Your lucky number is: 20

@app.route('/spell/<word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template('spell_word.html', word=caps_word)

@app.route('/form')
def show_form():
    return render_template('form.html')

COMPLIMENTS = ['cool', 'clever', 'tenacious', 'awesome', 'pythonic']

@app.route('/greet')
def get_greeting():
    username = request.args['username']
    nice_thing = choice(COMPLIMENTS)
    return render_template('greet.html', username=username, compliment=nice_thing)

@app.route('/form-2')
def show_form_2():
    return render_template('form_2.html')

@app.route('/greet-2')
def get_greeting_2():
    username = request.args['username']
    wants = request.args.get('wants_compliments')
    nice_things = sample(COMPLIMENTS, 3)
    return render_template('greet_2.html', username=username, wants_compliments=wants, compliments=nice_things)