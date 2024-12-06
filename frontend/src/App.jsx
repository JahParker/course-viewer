import './App.css';
import {useRoutes} from 'react-router-dom';
import {Login, Courses, CourseDetails, Welcome, SignUp } from './pages';

function App() {
  let pageRoutes = useRoutes([
    {
      path: "/",
      element:<Welcome />
    },
    {
      path:"/Signup",
      element: <SignUp />
    },
    {
      path:"/Login", // Remember to add useParams
      element: <Login /> 
    },
    {
      path:"/Courses",
      element: <Courses />
    },
    {
      path:"/:courseName", // Remember to add useParams
      element: <CourseDetails /> 
    },
  ]);

  return (
    <>
      {pageRoutes}
    </>
  );
}

export default App
