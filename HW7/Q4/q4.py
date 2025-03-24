"""
HW7 Q4
Gabrielle Sedlar
March 24, 2025

Task: Write a flask application that responds “Hello, User!” when accessing the root of your 
    application from a browser. However, when the root of your application is accessed via a 
    POST action, respond with “Hello, Computer!”. I should be able to access this 
    application at http://localhost:4356. 
    
"""

from flask import Flask

app = Flask(__name__)

@app.route('/') #when accessed on the brower, returns 'Hello, User!'
def index():
    return 'Hello, User!'
   
@app.route('/',methods=['POST']) #when accessed via POST action, returns 'Hello, Computer!'
def computer():
    return 'Hello, Computer!'

app.run(host='127.0.0.1',port=4356,debug=False)