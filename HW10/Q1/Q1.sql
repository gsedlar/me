"""
HW10 Q1
Gabrielle Sedlar
April 14, 2025
"""

CREATE TABLE IF NOT EXISTS pokemon(
    id integer PRIMARY KEY, 
    name text NOT NULL UNIQUE, 
    height integer, 
    weight integer, 
    base_experience integer
    )