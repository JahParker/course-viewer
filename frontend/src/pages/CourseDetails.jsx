import { Link } from "react-router-dom"
import Assignment from "../components/Cards/Assignment"
import Header from "../components/Header"
import Button from "../components/Button"

const CourseDetails = () => {
  return (
    <div className="course-detail">
      <Header />
        <div className="section-header">
          <div className="section-header-top">
            <h2>Course Name</h2>
            <h2>Course Grade: --</h2>
          </div>
          <div className="line-break" />
          <div className="section-header-bottom">
            <button>
              Edit Assignment Categories
            </button>
            <Button variant="add" />
        </div>
      </div>
      <div className="card-list">
          <Assignment />
          <Assignment />
          <Assignment />
      </div>
    </div>
  )
}

export default CourseDetails