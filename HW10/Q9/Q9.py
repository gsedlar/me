"""
HW10 Q9
Gabrielle Sedlar
April 14, 2025
"""

import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

db_path = 'Q9.db'

@app.route('/<pokemon>',methods=["GET"])
def get_pokemon(pokemon):
    
    q = "SELECT name, type_name FROM pokemon_types WHERE LOWER(name) = LOWER(?)" #get name and type(s) from pokemon_types table
    
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute(q, (pokemon,))
        results = c.fetchall()
        conn.close()
    
    except sqlite3.OperationalError:
        error_dict = dict(error='unable to connect to database')
        return jsonify(error_dict),500
    
    if not results:
        error_dict = dict(error='pokemon not found')
        return jsonify(error_dict),404
    
    name = results[0][0]
    types = ", ".join([row[1] for row in results])
    
    return jsonify({
        "name": name,
        "types": types
    })
        
    
    
app.run(host='127.0.0.1',port=9999,debug=True)