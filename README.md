# Course Grades

Final Project for Comp 267

## Getting started

```bash
git clone git@github.com:JahParker/course-viewer.git
cd course-viewer
```

### Frontend setup

#### Install dependencies

```bash
cd frontend
npm install
```

#### Run frontend server

```bash
npm run dev
```

### Backend setup

#### Install dependencies

```bash
cd backend
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Create a .env file within backend folder

Go [here](https://randomkeygen.com/) for a random key

```txt
# MySQL configuration
MYSQL_HOST=your-host-name
MYSQL_USER=your-username
MYSQL_PASSWORD=your-password
MYSQL_DB=your-database-name

# Secret key for Flask session management
SECRET_KEY=your-random-key
```

#### Run backend server

```bash
flask run
```

## Thoughts

Maybe a help button is called for. Just so users know how to use the app properly since the grade scale
 and category weights have to be edited upon creation.

Maybe, as an example, we can have the first value of a grading scale be 0 (id), 2 (course_id), A(letter_grade), 90 (min_score)
Upon editing, we can delete all records where the composite key is (0 (id), 2 (course_id)) then insert values based on input from the user.
 The same concept can be applied to assignment categories as well

There is no way to see if a class have been already created with the way we have it set up now.
 Is that really needed though? It would make it simpler if there are multiple students in a class.
  However, we can treat it like a hackathon presentation ("These are some things we've taken into consideration and would implement if we had more time").

AI was used for the decison making process of techstack, authentication tools, and project structure.

For the courses page, we need a table with course in student enrollment
 and the letter grade which will be calulated from the grades of the student assignments table 
 and the scores listed in the grade scale table

All the weights of the assignment should be equal to 100%
