import './App.css';
import {useRoutes} from 'react-router-dom';
import {Login, Courses, CourseDetails} from './pages';

function App() {
  let pageRoutes = useRoutes([
    {
      path: "/",
      element:<Login />
    },
    {
      path:"/Courses",
      element: <Courses />
    },
    {
      path:"/:CourseName", // Remember to add useParams
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
