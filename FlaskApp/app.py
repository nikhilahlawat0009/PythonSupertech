# ! /usr/bin/env python3     SHEBANG
# Author: Nikhil Ahlawat
# Version: 1.0
# Description: A flask app

"""
    Flask App with fun endpoints
"""

from flask import Flask, Response, request, render_template, url_for


# Create a Flask object

print(__name__)

app = Flask(__name__)

# Create some Endpoints/Routes
@app.route('/', methods=['GET'])
def hello_from_flask():
    return 'Hello from flask'

@app.route('/sky', methods=['GET'])
def hello_grads():
    return 'Hello sky grads'

@app.route('/get/text', methods=['GET'])
def get_text():
    return Response("Hello from Flask, using an explicit Response Object")

# Dynamic routes
@app.route('/dynamic/<string:word>')
def get_word(word):
    return word

@app.route('/square/<int:number>')
def get_square(number):
    return f"{number} squared in {number**2}"

@app.route('/hello/<string:name>')
def say_hello(name):
    return f"Hello {name}"

@app.route('/html/<string:name>')
def say_hello_html(name):
    return f"""
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <title>Sample - Flask routes</title>
     </head>
     <body>
         <h1>Name Page</h1>
         <p>Hello {name}!</p>
     </body>
     </html>
     """

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route("/index/<name>/<int:iq>")
def index(name, iq):
    url = url_for("get_text")
    return f"""
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <title>Sample - Flask routes</title>
     </head>
     <body>
         <h1>Name Page</h1>
         <p>Hello {name}!</p>
         <p>Your IQ is {iq}!</p>
         <hr>
         <a href="{url}">Welcome</a>
     </body>
     </html>
     """

if __name__ =="__main__":

    # Execute Only if ran directly as a program
    app.run(debug=True)



