import { useParams } from "react-router-dom"
import Assignment from "../components/Cards/Assignment"
import Header from "../components/Header"
import Button from "../components/Button"
import { useState, useEffect } from "react"


const CourseDetails = () => {
  const {courseName} = useParams();
  const [assignments, setAssignments] = useState(null); // Default to null

  const fetchData = async () => {
    try {
      const response = await fetch(`/api/${courseName}/assignments/get`, {
        method: 'GET',
        credentials: 'include', // or 'include' for cross-origin requests
    });
        const data = await response.json();
        
        // Ensure that the data is not null or empty before setting state
        if (data && data.length > 0) {
            setAssignments(data);
        } else {
            setAssignments([]); // If no data, set an empty array
        }
    } catch (error) {
      console.error('Error fetching data:', error);
      setAssignments([]); // Handle error by setting an empty array
    }
  }

  useEffect(() => {
    fetchData();
  }, []);

  const addAssignments = async () => {
    try {
      // Make the API request
      const response = await fetch('/api/courses/Math224%20Intro%20Probability%20and%20Statistics/assignments/add', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          assignment_name: "Homework 1",
          category_id: 1,
          score: 90
        })
      });
  
      // Check if the response is okay
      if (!response.ok) {
        throw new Error('Failed to add assignment');
      }
  
      const data = await response.json();
      console.log(data);
  
      // If successful, fetch the updated list of assignments and trigger re-render
      await fetchData(); // Assuming you have a function to fetch the assignments list
  
    } catch (error) {
      console.error('Error:', error);
    }
  }
  

  return (
    <div className="course-detail">
      {assignments && <Header user={assignments[0].student_name}/>}
        <div className="section-header">
          <div className="section-header-top">
            <h2>{courseName}</h2>
            {/* <h2>Course Grade: --</h2> */}
          </div>
          <div className="line-break" />
          <div className="section-header-bottom">
            <button>
              Edit Assignment Categories
            </button>
            <Button variant="add" onClick={addAssignments} />
        </div>
      </div>
      <div className="card-list">
        {assignments && assignments.map((assignment, index) => (
          <Assignment key={index} name={assignment.assignment_name} type={assignment.assignment_type} score={assignment.student_grade} />
          ))
        }
      </div>
    </div>
  )
}

export default CourseDetails