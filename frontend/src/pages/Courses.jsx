import { Link } from "react-router-dom";
import Button from "../components/Button";
import Course from "../components/Cards/Course";
import Header from "../components/Header";
import { useState, useEffect } from "react";

const Courses = () => {
  const [courses, setCourses] = useState(null); // Default to null
  const [isAdding, setIsAdding] = useState(false);
  const [courseName, setCourseName] = useState('');

  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/courses/get', {
        method: 'GET',
        credentials: 'include', // or 'include' for cross-origin requests
      });
      const data = await response.json();

      // Ensure that the data is not null or empty before setting state
      if (data && data.length > 0) {
        setCourses(data);
      } else {
        setCourses([]); // If no data, set an empty array
      }
    } catch (error) {
      console.error('Error fetching data:', error);
      setCourses([]); // Handle error by setting an empty array
    }

    console.log(`Fetched Courses: ${JSON.stringify(courses)}`);
  };

  useEffect(() => {
    fetchData();
  }, []); // Run the fetchData function when the component mounts
  
  const handleAddCourse = async () => {
    try {
      // Make the POST request to add a course
      const response = await fetch('http://localhost:8000/api/courses/add', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ courseName }),
        credentials: 'include',
      });

      const result = await response.json();
      if (result.message === 'SUCCESS') {
        console.log('Course added successfully!');
        // After adding the course, reload the courses list
        fetchData();  // Re-fetch courses after adding a new one
      }
    } catch (error) {
      console.error('Error adding course:', error);
    }
    setIsAdding(false);
    setCourseName('');
  };

  const addButton = () => {
    setIsAdding(true);
  };

  // Ensure you check that courses is not empty before accessing first_name

  return (
    <div className="courses">
      {courses && courses.length > 0 ? 
        <Header user={courses[0].first_name} />
      : 
        <Header user="--" />
      }
      <div className="section-header">
        <div className="section-header-top">
          <h2 id="section-h2">Courses</h2>
        </div>
        <div className="line-break" />
        <div id="section-button">
          <Button variant="add" onClick={addButton} />
        </div>
        {isAdding && 
          <div className="input">
            <input
              type="text"
              placeholder="Enter Course Name"
              value={courseName}
              onChange={(e) => setCourseName(e.target.value)}
            />
            <button onClick={handleAddCourse}>Submit</button>
          </div> 
        }
      </div>
      <div className="card-list">
        {courses && courses.length > 0 ? (
          courses.map((course, i) => (
            <div key={i} className="card-list-row">
              <Link  to={`/${course.course_name}`}>
                <Course courseName={course.course_name} />
              </Link>
              <button className="delete">
                X
              </button>
            </div>

          ))
        ) : (
          <p>No courses available</p>
        )}
      </div>
    </div>
  );
};

export default Courses;
