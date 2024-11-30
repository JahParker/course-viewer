import { Link } from "react-router-dom"
import Button from "../components/Button"
import Course from "../components/Cards/Course"
import Header from "../components/Header"

const Courses = () => {
  return (
    <div className="courses">
      <Header />
      <div className="section-header">
        <div className="section-header-top">
          <h2 id="section-h2">Courses</h2>
        </div>
        <div className="line-break" />
        <div id="section-button">
          <Button variant="add" />
        </div>
      </div>
      <div className="card-list">
        <Link to="/:CourseName">
          <Course />
        </Link>
        <Course />
        <Course />
      </div>
    </div>
  )
}

export default Courses