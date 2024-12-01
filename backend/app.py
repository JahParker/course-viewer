from flask import Flask, jsonify, session # Python web framework and Python to JSON
from flask_cors import CORS # Explained below
from dotenv import load_dotenv # Reads .env file
import os
import mysql.connector

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
CORS(app)  # Allows communication between our frontend and backend

# Create MySQL connection (What we've done in class)
def get_db_connection():
    # The values are coming from your .env file
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),  
        user=os.getenv('MYSQL_USER'),       
        password=os.getenv('MYSQL_PASSWORD'), 
        database=os.getenv('school_project') 
    )

# Example
# @app.route('/api/data/')
# def get_data():
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)
#     cursor.execute('SELECT * FROM my_table')  # Your MySQL query
#     rows = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return jsonify(rows)

# Authentication
@app.route('/api/login') 
def login():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})

@app.route('/api/logout')
def logout():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})


# Courses
@app.route('/api/courses')
def add_course():
    # Enrolls student in course
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})

@app.route('/api/courses')
def get_courses(): 
    # View all enrolled courses
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})

@app.route('/api/courses/<int:course_id>')
def edit_course(course_id): 
    # Update name of enrolled course
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})

@app.route('/api/courses/<int:course_id>')
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

@app.route('/api/courses/<int:course_id>/grade-scale')
def edit_grade_scale(course_id):
    # Set grade scale for a course
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})


# Assignments
@app.route('/api/courses/<int:course_id>/assignments')
def add_assignment(course_id):
    # Add assignment to student's course
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})

@app.route('/api/courses/<int:course_id>/assignments')
def get_assignments(course_id):
    # View all assignments assigned to a student in a course
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})

@app.route('/api/courses/<int:course_id>/assignments/<int:assignment_id>')
def edit_assignment(course_id, assignment_id): 
    # Update name, type, and score 
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})

@app.route('/api/courses/<int:course_id>/assignments/<int:assignment_id>')
def delete_assignment(course_id, assignment_id):
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

@app.route('/api/courses/<int:course_id>/categories')
def edit_categories(course_id):
    # Edit the assignment categor for a course
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})

@app.route('/api/courses/<int:course_id>/categories/<int:category_id>')
def delete_category(course_id, category_id):
    # Get the grade scale for a course
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})


# Grade
@app.route('/api/courses/<int:course_id>/letter-grade')
def get_grade(course_id, assignment_id):
    # Shows the letter grade based on scores of assignments in a course
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    
    
    cursor.close()
    connection.close()
    return jsonify({"message": "SUCCESS"})



if __name__ == '__main__':
    app.run(debug=True)
