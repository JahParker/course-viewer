import { useState } from "react";
import { useNavigate } from "react-router-dom";

const SignUp = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  // const handleLogin = async () => {
  //   try {
  //     const response = await fetch("http://localhost:8000/api/login", {
  //       method: "POST",
  //       headers: { "Content-Type": "application/json" },
  //       body: JSON.stringify({ username, password }),
  //       credentials: 'include',
  //     });

  //     const result = await response.json();

  //     if (response.ok) {
  //       // Navigate to the /Courses route if login is successful
  //       console.log("Login successful:", result);
  //       navigate("/Courses");
  //     } else {
  //       // Handle errors (e.g., invalid credentials)
  //       console.error("Login failed:", result.error);
  //       alert(result.error);
  //     }
  //   } catch (error) {
  //     console.error("Error:", error);
  //     alert("An unexpected error occurred.");
  //   }
  // };

  return (
    <div className="credentials">
      <h1>Sign Up</h1>
      <div className="form">
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <div className="radio">
          <input type="radio" id="student" name="user_type" value="student"/>
          <label htmlFor="student">Student</label>
          <br/>
          <input type="radio" id="professor" name="user_type" value="professor"/>
          <label htmlFor="professor">Professor</label>
        </div>
        <button onClick={null}>Sign up</button>
    </div>
  </div>
  );
};

export default SignUp;
