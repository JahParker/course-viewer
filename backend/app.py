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
CORS(app)

# Create MySQL connection (What we've done in class)
def get_db_connection():
    # The values are coming from your .env file
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),  
        user=os.getenv('MYSQL_USER'),       
        password=os.getenv('MYSQL_PASSWORD'), 
        database=os.getenv('MYSQL_DB') 
    )

# Authentication
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

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
            ''', (username, password)
        )
        student = cursor.fetchone()

        if not student:
            return jsonify({"error": "Student record not found"}), 404

        # Store the student ID in the session
        session['id'] = student['student_id']
        return jsonify({"message": "Login successful", "student_id": student['student_id']}), 200
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/api/logout')
def logout(): 
    session.pop('student_id', None) 
    return jsonify({"message": "SUCCESS"})


@app.route('/')

# Courses
@app.route('/api/courses/get')
def get_courses(): 
    # View all enrolled courses
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    student_id = 1
    print(student_id)
    
    # Joins the tables that show the courses associated with a particular student and calculate the letter grade
    # Whichever courses being use to get the letter grade is the same information needed to show the course info
    cursor.execute(
        '''
        SELECT 
        c.id AS course_id,
        c.name AS course_name,
        s.firstname AS first_name,
        lg.letter_grade
        FROM (
        SELECT 
            c.id AS course_id,
            SUM(sa.grade * (cat.weight / 100)) / SUM(cat.weight / 100) AS total_weighted_average
        FROM course c
        JOIN courseassignment ca ON c.id = ca.course_id_fk
        JOIN category cat ON ca.category_id_fk = cat.id
        JOIN studentassignment sa ON ca.id = sa.course_assignment_id_fk
        JOIN studentenrollment se ON c.id = se.course_id_fk
        WHERE se.student_id_fk = 1  
        GROUP BY 
            c.id
    ) AS category_avg
    JOIN course c ON category_avg.course_id = c.id
    JOIN student s ON s.id = %s 
    JOIN lettergradescale lg ON category_avg.total_weighted_average >= lg.min_score
WHERE 
    lg.min_score = (
        SELECT MAX(min_score) 
        FROM lettergradescale
        WHERE min_score <= category_avg.total_weighted_average
    )
ORDER BY course_id;

        ''', (student_id,)
    )
    # category_avg.total_weighted_average,
    courses = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return jsonify(courses)

@app.route('/api/courses/add', methods=['POST'])
def add_course():
    # Enrolls student in course
    data = request.json
    print('Data: ', data)
    student_id = 1
    course_name = data.get("course_name")
    
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
@app.route('/api/<course_name>/assignments/get')
def get_assignments(course_name):
    # View all assignments assigned to a student in a course
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    clean_course_name = unquote(course_name).strip()
    
    student_id = 1
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

        # Insert into studentassignment table (assigning to student with ID 1 for now)
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
