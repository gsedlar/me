"""
HW 8
Gabrielle Sedlar
March 24, 2025

wish me luck
"""

from flask import Flask, request
import csv
import os

app = Flask(__name__)

#creating function to create a new csv file and add data to it, got this from reddit lol
def write_to_csv(filename, data, headers):
    file_exists = os.path.exists(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(data)
        
#creating a delete function, also got this from reddit
def delete_from_csv(filename, id_key, id_value):
    rows = []
    
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    rows = [row for row in rows if row[id_key] != id_value]

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
        
#defining get function
def get_from_csv(filename, id_key, id_value):
    rows = []

    if not os.path.exists(filename):
        return 'no file exists'

    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    
    for row in rows:
        if row[id_key] == id_value:
            return row
    return None

@app.route('/student',methods=['POST','GET','DELETE'])
def student(): #ID, Name, Email, Phone, Year, Status 
    data = request.get_json() 
    
    if request.method == 'POST':
        if data.get('name') is None: 
            return 'name is required' 
        
        if data.get('id') is None:
            return 'id is required'
        
        if data.get('email') is None:
            return 'email is required'
        
        if data.get('phone') is None:
            return 'phone is required'
        
        if data.get('year') is None:
            return 'year is required'
        
        if data.get('status') is None:
            return 'status is required'
        
        student_data = { #writing dictionary for student data
            'id': data['id'],
            'name': data['name'],
            'email': data['email'],
            'phone': data['phone'],
            'year': data['year'],
            'status': data['status']
        }
    
        #writing student data to student.csv
        headers = ['id', 'name', 'email', 'phone', 'year','status']
        write_to_csv('student.csv', student_data, headers)
        
        return 'success!'
    
    elif request.method == 'DELETE':
        student_id = data.get('id')

        if student_id is None:
            return 'id is required for deletion', 500
        
        delete_from_csv('student.csv', 'id', student_id)
        return 'success!'
    
    #I HAVE NO CLUE WHY THIS WON'T WORK. everything i've seen says this should work, maybe it's that 
    #i'm not putting in enough data before deleting? but i'm not sure. same thing for all other delete requests
    
    elif request.method == 'GET':
        student_id = request.args.get('id') #get id from url
        if not student_id: #error if no student id
            return 'id is required', 500
        
        student_data = get_from_csv('student.csv', 'id', student_id)
        if student_data == None:
            return 'student data not found'
        else:
            return student_data

@app.route('/teacher',methods=['POST','GET','DELETE'])
def teacher(): #ID, Name, Email, Phone 
    data = request.get_json()
    
    if request.method == 'POST':
        #check all pieces of data present
        if data.get('name') is None: 
            return 'name is required',500 
        
        if data.get('id') is None:
            return 'id is required',500 
        
        if data.get('email') is None:
            return 'email is required',500 
        
        if data.get('phone') is None:
            return 'phone is required',500 
        
        teacher_data = { #writing dictionary for teacher data
            'id': data['id'],
            'name': data['name'],
            'email': data['email'],
            'phone': data['phone'],
        }
    
        #writing teacher data to teacher.csv
        headers = ['id', 'name', 'email', 'phone']
        write_to_csv('teacher.csv', teacher_data, headers)
        
        return 'success!'
    
    elif request.method == 'DELETE':
        teacher_id = data.get('id')

        if teacher_id is None:
            return 'id is required for deletion', 500
        
        delete_from_csv('teacher.csv', 'id', teacher_id)
        return 'success!'
    
    elif request.method == 'GET':
        if 'count' == 'true': #if the user wants to do a count, it automatically does the count, not get id.
            class_rows = []

                
        with open('class.csv', mode='r', newline='') as file: #reading the class file to see how many classes the teacher teaches
            reader = csv.DictReader(file)
            class_rows = list(reader)

            #filtering only classes that belong to the teacher, got this piece online
            teacher_classes = [cls for cls in class_rows if cls['teacherID'] == teacher_id]
            teacher_data['count'] = len(teacher_classes)

            return teacher_data
        teacher_id = request.args.get('id') #get id from url
        if not teacher_id: #error if no teacher id
            return 'id is required', 500
        
        teacher_data = get_from_csv('teacher.csv', 'id', teacher_id)
        if teacher_data == None:
            return 'teacher data not found'
        else:
            return teacher_data


@app.route('/class',methods=['POST','GET','DELETE'])
def classroom(): #ID, Name, Department, TeacherID 
    
    if request.method == 'POST':
        data = request.get_json()
        
        if data.get('name') is None: 
            return 'name is required' ,500 
        
        if data.get('id') is None:
            return 'id is required',500 
        
        if data.get('department') is None: 
            {'department':'Misc'}
        
        if data.get('teacherID') is None:
            return 'teacherID is required',500 
        
        class_data = { #writing dictionary for class data
            'id': data['id'],
            'name': data['name'],
            'department': data['department'],
            'teacherID': data['teacherID'],
        }
    
        #writing class data to class.csv
        headers = ['id', 'name', 'department', 'teacherID']
        write_to_csv('class.csv', class_data, headers)
        
        return 'success!'
    
    elif request.method == 'DELETE':
        class_id = request.args.get('id')  #from query parameters

        if class_id is None:
            return 'id is required for deletion', 500
        
        delete_from_csv('class.csv', 'id', class_id)
        
    elif request.method == 'GET':
        if 'count' == True:
            count = 0
            for r in 'class.csv'.itterrows():
                count = count + 1
            return '{count:' + count + '}'
           
        class_id = request.args.get('id') #get id from url
        if class_id is None: #error if no class id
            return 'id is required', 500
        
        class_data = get_from_csv('class.csv', 'id', class_id)
        if class_data == None:
            return 'class data not found'
        else:
            return class_data
        
    
        
    
app.run(host='127.0.0.1',port=9999,debug=False)
