# Set up your imports here!
from flask import Flask

app = Flask(__name__)
@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return '<h1>Welcome! Go to puppy_latin/name to see your name in puppy latin</h1>'

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    if name[-1]!='y':
        puppylatin_name = name + 'y'
    else:
        puppylatin_name = name[:-1] + 'iful'
    return f'<h1>Hi, {name}. Your puppylatin name is {puppylatin_name}.</h1>'
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"


if __name__ == '__main__':
    app.run()
