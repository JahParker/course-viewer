import { useState } from "react"
import Button from "../Button";

const Course = () => {
  let [isEditing, setIsEditing] = useState(false);

  return (
    <div className="card">
      {isEditing ? 
        <input type="text" name="course title" id="course title" /> 
      : 
        <h3>Course Title</h3> 
      }

      <div className="grade">
        <p>Grade: A</p>
      </div>
      
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