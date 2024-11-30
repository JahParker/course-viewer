import { Link } from "react-router-dom";

const Header = () => {
  return (
    <>
      <Link to="/Courses">
        <h1>Title</h1>
      </Link>
      <div className="user-account">
        <p>Welcome, ---</p>
        <Link to="/">
          <button className="signout">
            {"(Sign out)"}
          </button>
        </Link>
      </div>
    </>
  )
}

export default Header;