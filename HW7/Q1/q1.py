"""
HW7 Q1
Gabrielle Sedlar
March 20, 2025

Task: Create a flask application that responds with “Hello, <Pokemon>!”. Where <Pokemon> is 
    the name of a random pokemon found in the `pokemon.csv` data file that we’ve been 
    working with in previous assignments. I should be able to hit your application at 
    `http://localhost:5690` and receive my desired response.
    
"""

import pandas as pd
from flask import Flask
import random as random

p = pd.read_csv('../data/pokemon.csv')

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, ' + p.iloc[random.randint(0,len(p))]['identifier']
    #returns a random pokemon in the dataframe

app.run(host='127.0.0.1',port=5690,debug=False)

