import { Link, useNavigate } from "react-router-dom"; // Add useHistory for redirection
import { useState } from "react"; // Import useState for managing user state

const Header = ({ user }) => {
  const [isLoggedOut, setIsLoggedOut] = useState(false);
  const navigate = useNavigate(); // Correct usage of useNavigate

  const handleLogout = async () => {
    try {
      // Make the logout request to the backend
      const response = await fetch('http://localhost:8000/api/logout', {
        method: 'POST', // Use POST for logout to avoid caching issues
        credentials: 'include', // Include credentials for session management
      });

      const data = await response.json();

      if (data.message === "SUCCESS") {
        setIsLoggedOut(true);
        navigate("/"); // Redirect to the homepage or login page
      }
    } catch (error) {
      console.error('Error logging out:', error);
    }
  };

  return (
    <>
      <Link to="/Courses">
        <h1>Course Viewer</h1>
      </Link>
      <div className="user-account">
        <p>Welcome, {user}</p>
        <button className="signout" onClick={handleLogout}>
          {"Sign out"}
        </button>
      </div>
    </>
  );
};

export default Header;
