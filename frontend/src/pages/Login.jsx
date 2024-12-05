import { Link } from 'react-router-dom';

const Login = () => {
  return (
    <div className="login">
      <h1>Course Viewer</h1>
      <div className="form">
        <input type="text" />
        <input type="text" />
      </div>

      <Link to="/Courses">
        <button>Submit</button>
      </Link>
    </div>
  )
}

export default Login