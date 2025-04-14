"""
HW9
Gabrielle Sedlar
April 7, 2025
"""


from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

db_path = ('data/school.db')

@app.route('/student',methods=['POST','GET','DELETE']) #student accepts post, get, and delete
def student():
    data = request.get_json()
    if request.method == 'POST': #post adds a student
        
        pname = data.get('name')
        pid = data.get('id')
        pemail = data.get('email')
        pphone = data.get('phone')
        pstatus = data.get('status')
        pyear = data.get('year')
        
        #add a student with all 6 values
        student_data = "INSERT INTO STUDENT(id,name,email,phone,year,status) VALUES('{i}','{n}','{e}','{p}','{y}','{s}')".format(n=pname,i=pid,e=pemail,p=pphone,y=pyear,s=pstatus);
        
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute(student_data)
            conn.commit()
            conn.close()
            ret_data = dict(success=True,id=pid)
            return jsonify(ret_data)
        except Exception as e:
            print(e)
            return jsonify("{'error':'all fields required'}"),500 #if a field isn't there, it returns an error
        
    elif request.method == 'DELETE': #delete a student based on id
        data = request.get_json()
        student_id = data.get('id')

        if not student_id:
            return jsonify({'error': 'id is required'}), 500 #if id not given, error message is returned
        
        del_student = "DELETE FROM student WHERE id = ?",(student_id) #putting ? allows for one parameter to be a variable
        
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute(del_student)
            conn.commit()
            conn.close()
            ret_data = dict(success=True,id=student_id)
            return jsonify(ret_data) #returns id of student deleted

        except Exception as e:
            print(e)
            return jsonify({'error': 'Failed to delete student'}), 500
    
    
    elif request.method == 'GET': #return a student's data
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.row_factory = sqlite3.Row
            cursor.execute("SELECT * FROM student WHERE id = ?", (id)) #user decides on the ID to return
            student = cursor.fetchone() #should only have one per id, so will return the only one

            if student:
                student_data = dict(student)
                return jsonify(student_data) #returns the data for that student
            else:
                return jsonify({'error': 'Student not found'}), 404

        except Exception as e:
            print(e)
            return jsonify({'error': 'Failed to retrieve student'}), 500
        
    
@app.route('/teacher',methods=['POST','GET','DELETE']) #mostly same thing for teacher as for student
def teacher():
    data = request.get_json()
    if request.method == 'POST': #post method adds a teacher
        
        pname = data.get('name')
        pid = data.get('id')
        pemail = data.get('email')
        pphone = data.get('phone')
        
        teacher_data = "INSERT INTO TEACHER(id,name,email,phone) VALUES('{i}','{n}','{e}','{p}')".format(n=pname,i=pid,e=pemail,p=pphone);
        
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute(teacher_data)
            conn.commit()
            conn.close()
            ret_data = dict(success=True,id=pid)
            return jsonify(ret_data)
        except Exception as e:
            print(e)
            return jsonify("{'error':'all fields required'}"),500
        
        
    elif request.method == 'DELETE': #delete a teacher based on id
        data = request.get_json()
        teacher_id = data.get('id')

        if not teacher_id:
            return jsonify({'error': 'id is required'}), 500
            
        del_teacher = "DELETE FROM teacher WHERE id = ?",(teacher_id)
        
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute(del_teacher)
            conn.commit()
            conn.close()
            ret_data = dict(success=True,id=teacher_id)
            return jsonify(ret_data)

        except Exception as e:
            print(e)
            return jsonify({'error': 'Failed to delete teacher'}), 500
    
    elif request.method == 'GET': #question 19, counts the number of classes a teacher teaches
        
        count = request.args.get('count', '').lower()

        if count == 'true':
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.row_factory = sqlite3.Row
                c.execute("SELECT COUNT(*) FROM class WHERE teacherID = ?", (id,))
                teacher_class_count = c.fetchone()[0]
    
                c.execute("SELECT * FROM teacher WHERE id = ?", (id,))
                teacher = c.fetchone()
    
                if teacher:
                    teacher_data = dict(teacher)
                    teacher_data['count'] = teacher_class_count
                    return jsonify(teacher_data)
                else:
                    return jsonify({'error': 'Teacher not found'}), 404
    
            except Exception as e:
                print(e)
                return jsonify({'error': 'Failed to retrieve teacher or class count'}), 500
    
        else: #returns a teacher's data, same as for student, but only if count = false
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.row_factory = sqlite3.Row
                c.execute("SELECT * FROM teacher WHERE id = ?", (id,))
                teacher = c.fetchone()

                if teacher:
                    teacher_data = dict(teacher)
                    return jsonify(teacher_data)
                else:
                    return jsonify({'error': 'Teacher not found'}), 404
        
            except Exception as e:
                print(e)
                return jsonify({'error': 'Failed to retrieve teacher'}), 500


    
@app.route('/class',methods=['POST','GET','DELETE']) #very similar to student and teacher, small differences
def classroom(): 
    data = request.get_json()        
    
    if request.method == 'POST':
        
        pname = data.get('name')
        pid = data.get('id')
        pdep = data.get('department','Misc') #department defaults to Misc if nothing is given
        pteach = data.get('teacherID')
        
        class_data = "INSERT INTO CLASS(id,name,department,teacherID) VALUES('{i}','{n}','{d}','{t}')".format(n=pname,i=pid,d=pdep,t=pteach);
        
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute(class_data)
            conn.commit()
            conn.close()
            ret_data = dict(success=True,id=pid)
            return jsonify(ret_data)
        except Exception as e:
            print(e)
            return jsonify("{'error':'all fields required'}"),500
        
    
    elif request.method == 'DELETE':
        class_id = request.args.get('id') #delete class from query params

        if not class_id:
            return jsonify({'error': 'id query parameter is required'}), 500
        
        del_class = "DELETE FROM class WHERE id = ?",(class_id)
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute(del_class)
            conn.commit()
            conn.close()
            ret_data = dict(success=True,id=class_id)
            return jsonify(ret_data)

        except Exception as e:
            print(e)
            return jsonify({'error': 'Failed to delete class'}), 500
    
    
    elif request.method == 'GET':
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.row_factory = sqlite3.Row
            c.execute("SELECT * FROM class WHERE id = ?", (id,))
            classroom = c.fetchone()
            
            if classroom: #classroom variable bc class is reserved in python
                class_data = dict(class_data)
                return jsonify(class_data)
            else:
                return jsonify({'error': 'Class not found'}), 404

        except Exception as e:
            print(e)
            return jsonify({'error': 'Failed to retrieve class'}), 500
        
        #question 18, count the number of classes
        count = request.args.get('count', '').lower()
    
        if count == 'true':
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.row_factory = sqlite3.Row
                c.execute("SELECT COUNT(*) FROM class")
                class_count = c.fetchone()[0]
                return jsonify({'count': class_count})
    
            except Exception as e:
                print(e)
                return jsonify({'error': 'Failed to retrieve class count'}), 500
    
#these two are added on the end bc they require different endpoints than the other questions
#question 20, allow user to change phone number of teacher or student
@app.route('/student/update_phone', methods=['GET'])
def update_student_phone():
    student_id = request.args.get('id')
    new_phone = request.args.get('phone')

    if not student_id or not new_phone:
        return jsonify({'error': 'Both id and phone parameters are required'}), 400

    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.row_factory = sqlite3.Row
        c.execute("UPDATE student SET phone = ? WHERE id = ?", (new_phone, student_id))
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'id': student_id, 'updated_phone': new_phone})

    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to update student phone number'}), 500


# 20. Update phone number for teacher
@app.route('/teacher/update_phone', methods=['GET'])
def update_teacher_phone():
    teacher_id = request.args.get('id')
    new_phone = request.args.get('phone')

    if not teacher_id or not new_phone:
        return jsonify({'error': 'Both id and phone parameters are required'}), 400

    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.row_factory = sqlite3.Row
        c.execute("UPDATE teacher SET phone = ? WHERE id = ?", (new_phone, teacher_id))
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'id': teacher_id, 'updated_phone': new_phone})

    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to update teacher phone number'}), 500
    

    
app.run(host='127.0.0.1',port=9999,debug=True)