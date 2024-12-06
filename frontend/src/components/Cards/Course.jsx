import { useState } from "react"
import Button from "../Button";

const Course = ({ courseName }) => {
  let [isEditing, setIsEditing] = useState(false);

  return (
    <div className="card">
      {isEditing ? 
        <input type="text" name="course title" id="course title" /> 
      : 
        <h3>{courseName}</h3> 
      }

      {/* <div className="grade">
        <p>Grade: {letterGrade}</p>
      </div> */}
      
      {isEditing ? 
        <div className="actions">
          <Button variant={"submit"} />
          <Button variant={"cancel"} />
          <Button variant={"delete"} />
        </div>
      : 
       <img src="" alt="" onClick={null}/>
      }
    </div>
  )
}

export default Course;