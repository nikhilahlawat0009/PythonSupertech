# ! /usr/bin/env python3     SHEBANG
# Author: Nikhil Ahlawat
# Version: 1.0
# Description:


from flask import render_template
from .import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')
@app.route('/words')
def template_words():
    words = []
    fh_in = open(r"/Users/nan707/Documents/PythonPrograms/words", mode="rt")
    for word in fh_in:
        if "town" in word:
            words.append(word)
    return render_template('words.html', words=words)