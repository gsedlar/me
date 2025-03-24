"""
HW7 Q5
Gabrielle Sedlar
March 24, 2025

Task: Write a flask application that represents a pokemon team management system. There 
    should be endpoints `create`, `list` and `delete` that allow you to generate a random 
    team, show that random team and delete that random team. Each of the endpoints 
    should accept only their respective HTTP method. If a random team already exists, you 
    should return a message telling the user that a team already exists. I should be able to 
    access these endpoints at http://localhost:8989. 
    
"""

from flask import Flask
import pandas as pd

p = pd.read_csv('../data/pokemon.csv')

app = Flask(__name__)

team = [] #empty list for team

@app.route('/create') #generates a random team
def create():
    global team #can edit team inside the function and it modified the outside variable too
    if len(team) != 0:
        return 'Team already exists.'
    team = p.sample(50)['identifier'].tolist()
    return 'Team successfully created.'
   
@app.route('/list') #shows the random team
def list():
    if len(team) == 0:
        return 'No team created yet.'
    return team

@app.route('/delete') #delete the random team
def delete():
    global team
    team = [] #returns the team to an empty list
    return 'Team successfully deleted.'

app.run(host='127.0.0.1',port=8989,debug=False)