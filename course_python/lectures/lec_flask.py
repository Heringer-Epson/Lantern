import numpy as np
import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return('aloi')

@app.route('/homepage')
def hp():
    #return('<h2> This is homepage </h2>')
    return('<marquee> This is homepage </marquee>')

@app.route('/profile/<username>')
def profile(username):
    return('Hello %s' %username ) 

@app.route('/blog/<inp_id>')
def post(inp_id):
    return('Post ID is %s' %inp_id)

if __name__=='__main__':
    app.run(debug=True)
