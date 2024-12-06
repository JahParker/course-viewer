import time
from flask import Flask, jsonify, session, request # Python web framework and Python to JSON
from flask_cors import CORS # Explained below
from dotenv import load_dotenv # Reads .env file
import os
import mysql.connector
from urllib.parse import unquote

load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Allows communication between our frontend and backend
CORS(app, resources={r"/*": {"origins": "http://localhost:5173", "supports_credentials": True}})

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
    return response

# Create MySQL connection (What we've done in class)
def get_db_connection():
    # The values are coming from your .env file
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),  
        user=os.getenv('MYSQL_USER'),       
        password=os.getenv('MYSQL_PASSWORD'), 
        database=os.getenv('MYSQL_DB') 
    )

# Authentication (TODO: Add ability to detect role of user)
@app.route('/api/register', methods=['POST'])
def register():
    # Takes the data from the request and stores them in variables
    data = request.json
    username = data.get("username")
    password = data.get("password")
    role = data.get("role")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # Checks if auth id and student auth id match
        cursor.execute(
            '''
            
            ''', (username, password, role)
        )
        student = cursor.fetchone()

        # Store the student ID in the session
        # session['id'] = student['student_id']
        # print(session['id'])
        
        return jsonify({"message": "Login successful", "student_id": student['student_id']}), 200
    
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()



@app.route('/api/login', methods=['POST'])
def login():
    # Takes the data from the request and stores them in variables
    data = request.json
    username = data.get("username")
    password = data.get("password")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # Checks if auth id and student auth id match
        cursor.execute(
            '''
            SELECT student.id AS student_id
            FROM authentication
            JOIN student ON authentication.id = student.authentication_id_fk
            WHERE authentication.username = %s AND authentication.password = %s
            ''', (username, password,)
        )
        student = cursor.fetchone()
        print(student)
        
        # Check if the query returned a result
        if student:
            # Store the student ID in the session
            session["student_id"] = student['student_id']
            return jsonify({"message": "Login successful", "student_id": student['student_id']}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401
    
    except Exception as e:
        return jsonify({"error": "Database error: " + str(e)}), 500
    finally:
        cursor.close()
        connection.close()


@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()  # Clears session data
    print(dict(session))
    return jsonify({"message": "SUCCESS"})


# Courses
@app.route('/api/courses/get', methods=['GET'])
def get_courses(): 
    # Ensure that the student_id is retrieved from the session
    student_id = session.get('student_id')
    print('Id of student: ', student_id)
    
    if not student_id:
        return jsonify({"error": "User not logged in"}), 401
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # Retrieve the student's name and courses they are enrolled in
        cursor.execute(
            '''
            SELECT 
                c.id AS course_id,
                c.name AS course_name,
                s.firstname AS first_name,
                s.lastname AS last_name
            FROM course c
            JOIN studentenrollment se ON c.id = se.course_id_fk
            JOIN student s ON s.id = se.student_id_fk
            WHERE se.student_id_fk = %s
            ORDER BY c.id;
            ''', (student_id,)
        )

        courses = cursor.fetchall()
        print(f"Fetched courses: {courses}")
        
        if courses:
            return jsonify(courses), 200
        else:
            return jsonify({"message": "No courses found"}), 404

    except Exception as e:
        return jsonify({"error": "Database error: " + str(e)}), 500
    
    finally:
        cursor.close()
        connection.close()



@app.route('/api/courses/add', methods=['POST'])
def add_course():
    # Enrolls student in course
    data = request.json
    student_id = session.get('student_id')
    course_name = data.get("courseName")
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    ## Takes the names from the front end and inserts into the course table
    cursor.execute(
        '''
        INSERT INTO course (name)
        VALUES (%s)
        ''', (course_name,)
    )
    
    connection.commit()
    
    course_id = cursor.lastrowid
    
    # Once the course is created, the logged in student is immediately 
    cursor.execute(
        '''
        INSERT INTO studentenrollment (student_id_fk, course_id_fk)
        VALUES (%s, %s)
        ''', (student_id, course_id,)
    )
    
    connection.commit()
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})


# @app.route('/api/courses/<int:course_id>')
# def edit_course(course_id): 
#     # Update name of enrolled course
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)
    
    
    
#     cursor.close()
#     connection.close()
#     return jsonify({"message": "SUCCESS"})

@app.route('/api/courses/<int:course_id>/delete')
def delete_course(course_id): 
    # Unenroll in course (Remove all related data)
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})


# Grade Scale
@app.route('/api/courses/<int:course_id>/grade-scale')
def get_grade_scale(course_id):
    # Get the grade scale for a course
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})

# @app.route('/api/courses/<int:course_id>/grade-scale')
# def edit_grade_scale(course_id):
#     # Set grade scale for a course
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)
    
    
    
#     cursor.close()
#     connection.close()
#     return jsonify({"message": "SUCCESS"})


# Assignments
@app.route('/api/<course_name>/assignments/get', methods=['GET'])
def get_assignments(course_name):
    # View all assignments assigned to a student in a course
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    student_id = session.get('student_id')
    
    clean_course_name = unquote(course_name).strip()
    
    # Grabs the assignment linked in a course, the category, and student information
    cursor.execute(
        '''
        SELECT
            courseassignment.id AS assignment_id,
            courseassignment.name AS assignment_name,
            courseassignment.subname AS assignment_subname,
            courseassignment.category_id_fk AS category_id,
            category.type AS assignment_type,
            student.firstname AS student_name,
            studentassignment.grade AS student_grade
        FROM studentassignment
        JOIN courseassignment ON studentassignment.course_assignment_id_fk = courseassignment.id
        JOIN course ON courseassignment.course_id_fk = course.id
        JOIN category ON courseassignment.category_id_fk = category.id
        JOIN student ON studentassignment.student_id_fk = student.id
        WHERE course.name = %s AND studentassignment.student_id_fk = %s
        ''', (course_name, student_id)
    )
    
    assignments = cursor.fetchall()
    print(f"Fetched assignments: {assignments}")
    cursor.close()
    connection.close()
    return jsonify(assignments)

@app.route('/api/courses/<course_name>/assignments/add', methods=['POST'])
def add_assignment(course_name):
    # Get assignment data from the request
    data = request.json
    assignment_name = data.get("assignment_name")
    category_id = data.get("category_id")
    score = data.get("score")

    # Validate input
    if not assignment_name or not category_id or score is None:
        return jsonify({"error": "Missing required fields: 'assignment_name', 'category_id' or 'score'"}), 400

    try:
        # Establish database connection
        student_id = session.get('student_id')
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # Clean the course name from URL encoding
        clean_course_name = unquote(course_name).strip()

        # Check if course exists
        cursor.execute("SELECT id FROM course WHERE name = %s", (clean_course_name,))
        course = cursor.fetchone()

        if not course:
            return jsonify({"error": f"Course '{clean_course_name}' not found"}), 404

        course_id = course['id']

        # Insert into courseassignment table
        cursor.execute(
            '''
            INSERT INTO courseassignment (course_id_fk, name, category_id_fk, score)
            VALUES (%s, %s, %s, %s)
            ''', (course_id, assignment_name, category_id, score)
        )

        assignment_id = cursor.lastrowid

        # Insert into studentassignment table
        cursor.execute(
            '''
            INSERT INTO studentassignment (student_id_fk, course_assignment_id_fk)
            VALUES (%s, %s)
            ''', (student_id, assignment_id)
        )

        # Commit transaction
        connection.commit()

    except Exception as e:
        # Rollback and handle any errors
        connection.rollback()
        cursor.close()
        connection.close()
        return jsonify({"error": f"Failed to add assignment: {str(e)}"}), 500

    # Close resources
    cursor.close()
    connection.close()

    # Return success message
    return jsonify({"message": "SUCCESS"}), 200

# @app.route('/api/courses/<int:course_id>/assignments/<int:assignment_id>')
# def edit_assignment(course_id, assignment_id): 
#     # Update name, type, and score 
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)
    
    
    
#     cursor.close()
#     connection.close()
#     return jsonify({"message": "SUCCESS"})

@app.route('/api/courses/<course_name>/assignments/<int:assignment_id>')
def delete_assignment(course_name, assignment_id):
    # Delete an assignment assigned to a student in a course
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})


# Categories
@app.route('/api/courses/<int:course_id>/categories')
def add_category(course_id):
    # Add an assignment category
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})

@app.route('/api/courses/<int:course_id>/categories')
def get_categories(course_id):
    # Get the assignment categories for a course
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})

# @app.route('/api/courses/<int:course_id>/categories')
# def edit_categories(course_id):
#     # Edit the assignment categor for a course
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)
    
    
    
#     cursor.close()
#     connection.close()
#     return jsonify({"message": "SUCCESS"})

@app.route('/api/courses/<int:course_id>/categories/<int:category_id>')
def delete_category(course_id, category_id):
    # Get the grade scale for a course
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})


# Grade
# @app.route('/api/courses/<course_name>/letter-grade')
# def get_grade(course_id, assignment_id):
#     # Shows the letter grade based on scores of assignments in a course
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)
    
#     cursor.execute(
#         '''
#         SELECT 
#             course_id,
#             course_name,
#             total_weighted_average,
#             lg.letter_grade
#         FROM (
#             SELECT 
#                 c.id AS course_id,
#                 c.name AS course_name,
#                 SUM(sa.grade * (cat.weight / 100)) / SUM(cat.weight / 100) AS total_weighted_average
#             FROM course c 
#             JOIN courseassignment ca ON c.id = ca.course_id_fk
#             JOIN category cat ON ca.category_id_fk = cat.id
#             JOIN studentassignment sa ON ca.id = sa.course_assignment_id_fk
#             GROUP BY c.id, c.name
#         ) AS category_avg
#         JOIN lettergradescale lg ON category_avg.total_weighted_average >= lg.min_score
#         WHERE lg.min_score = (
#             SELECT MAX(min_score) 
#             FROM lettergradescale
#             WHERE min_score <= category_avg.total_weighted_average
#         )
#         ORDER BY course_id;

#         '''
#     )
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})



if __name__ == '__main__':
    app.run(port=8000, debug=True)
