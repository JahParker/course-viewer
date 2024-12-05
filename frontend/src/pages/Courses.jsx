import { Link } from "react-router-dom"
import Button from "../components/Button"
import Course from "../components/Cards/Course"
import Header from "../components/Header"
import { useState, useEffect } from "react"

const Courses = () => {
  // Method to get data from API goes here
  const [courses, setCourses] = useState(null); // Default to null

  const fetchData = async () => {
      try {
          const response = await fetch('http://localhost:8000/api/courses/get');
          const data = await response.json();
          
          // Ensure that the data is not null or empty before setting state
          if (data && data.length > 0) {
              setCourses(data);
          } else {
              setCourses([]); // If no data, set an empty array
          }
          console.log(data);
      } catch (error) {
          console.error('Error fetching data:', error);
          setCourses([]); // Handle error by setting an empty array
      }
  }

  useEffect(() => {
      fetchData();
  }, []); // Run the fetchData function when the component mounts
  
  const addCourse = async () => {
    try {
      // Make the POST request to add a course
      const response = await fetch('http://localhost:8000/api/courses/add', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          course_name: "Intro Programming",
        }),
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
  };

  return (
    <div className="courses">
      {courses && <Header user={courses[0].first_name} />}
      <div className="section-header">
        <div className="section-header-top">
          <h2 id="section-h2">Courses</h2>
        </div>
        <div className="line-break" />
        <div id="section-button">
          <Button variant="add" onClick={addCourse} />
        </div>
      </div>
      <div className="card-list">
          {console.log(courses)}
          {courses && courses.map((course, index) => (
            <Link key={index} to={`/${course.course_name}`}>
              <Course courseName={course.course_name} letterGrade={course.letter_grade}/>
            </Link>
          ))}
      </div>
    </div>
  )
}

export default Courses