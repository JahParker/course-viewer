import { Link } from "react-router-dom";

const Header = ({user}) => {
  return (
    <>
      <Link to="/Courses">
        <h1>Course Viewer</h1>
      </Link>
      <div className="user-account">
        <p>Welcome, {user} </p>
        <Link to="/">
          <button className="signout">
            {"Sign out"}
          </button>
        </Link>
      </div>
    </>
  )
}

export default Header;