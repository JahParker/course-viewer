import { Link } from "react-router-dom";


const Welcome = () => {
  return (
    <div className="login">
      <h1>Course Viewer</h1>
      <div className="button-container">
        <Link to="/Signup">
          <button >Sign up</button>
        </Link>
        <Link to="/Login">
          <button >Log in</button>
        </Link>
      </div>
    </div>
  );
};

export default Welcome;
