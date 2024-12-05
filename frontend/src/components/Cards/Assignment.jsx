import { useState } from "react"
import Button from "../Button";

const Assignment = ({name, type, score}) => {
  let [isEditing, setIsEditing] = useState(false);

  return (
    <div className="card">
      {isEditing ? 
        <>
          <input type="text" name="assignment name" id="" />

          <h3>Category:</h3>
          <div className="dropdown">
            <button onClick={null} className="dropbtn">
              {type}
            </button>
            <div id="dropdown-list" className="dropdown-content">
              <p onClick={null}>Link 1</p>
              <p onClick={null}>Link 2</p>
              <p onClick={null}>Link 3</p>
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
          <h3>{name}</h3>
          <h3>Category:</h3>
          <p>{type}</p>
          <h3>Score:</h3>
          <p>{score}</p>
          <img src="" alt="" onClick={null}/>
        </>
      }
    </div>
  )
}

export default Assignment;