"""
HW7 Q6
Gabrielle Sedlar
March 24, 2025

Task: Expanding on Q5, let’s start doing some basic logging to a file. Using tooling that we 
    already know, let’s write each action that our API takes to a file called out.log. When an 
    action is taken (create, list, or delete) write a log following this example: 
        
        Action - HTTP_METHOD - <pokmon> (added/deleted/etc)
    
"""

from flask import Flask
import pandas as pd

p = pd.read_csv('../data/pokemon.csv')

app = Flask(__name__)

team = [] #empty list for team
file = open('out.log','w')

@app.route('/create') #generates a random team
def create():
    global team #can edit team inside the function and it modified the outside variable too
    if len(team) != 0:
        return 'Team already exists.'
    team = p.sample(50)['identifier'].tolist()
    file.write('Action - HTTP_METHOD - <pokmon> (added)')
    return 'Team successfully created.'
   
@app.route('/list') #shows the random team
def list():
    if len(team) == 0:
        return 'No team created yet.'
    file.write('Action - HTTP_METHOD - <pokmon> (listed)')
    return team

@app.route('/delete') #delete the random team
def delete():
    global team
    team = [] #returns the team to an empty list
    file.write('Action - HTTP_METHOD - <pokmon> (deleted)')
    return 'Team successfully deleted.'


app.run(host='127.0.0.1',port=8989,debug=False)

file.close()