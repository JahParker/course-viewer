import { useState } from "react"
import Button from "../Button";

const Assignment = () => {
  let [isEditing, setIsEditing] = useState(false);

  return (
    <div className="card">
      {isEditing ? 
        <>
          <input type="text" name="assignment name" id="" />

          <h3>Category:</h3>
          <div class="dropdown">
            <button onClick={toggleDropdown} class="dropbtn">
              Type
            </button>
            <div id="dropdown-list" class="dropdown-content">
              <p onClick={}>Link 1</p>
              <p onClick={}>Link 2</p>
              <p onClick={}>Link 3</p>
            </div>
          </div>

          <h3>Score:</h3>
          <input type="text" name="score" id="" />
          
          <div className="actions">
            <Button variant={"submit"} />
            <Button variant={"cancel"} />
            <Button variant={"delete"} />
          </div>
        </>
      : 
        <>
          <h3>Assignment Name</h3>
          <h3>Category:</h3>
          <p>Type</p>
          <h3>Score:</h3>
          <p>--</p>
          <img src="" alt="" onClick={}/>
        </>
      }
    </div>
  )
}

export default Assignment;