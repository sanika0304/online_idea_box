## **Project Description**

**Online Idea Box** is a web-based platform designed to streamline idea collection, feedback, and communication between students, faculty, and administrators within an educational institution. The system provides a centralized space where users can submit innovative suggestions or raise concerns, and administrators can track, respond to, and manage those submissions efficiently.

The project features role-based access:

* **Students & Faculty** can register, log in, and submit ideas.
* **Admins** have a dedicated dashboard to view all submissions, update their status (like *Viewed*, *In Process*, or *Completed*), and send personalized replies.

It includes:
* A login/signup system with user roles.
* A clean and responsive user interface with dark transparent containers.
* Status tags with color badges for better visual feedback.
* PDF export functionality for saving idea records.
* Secure backend built with Flask and SQL Server for managing data.

This project encourages active participation and transparency in institutional development by making idea sharing accessible, organized, and trackable.

## **Project Structure**

```
online-idea-box/
│
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
│
├── static/                         # Static files (CSS, images, JS)
│   ├── style.css                   # Global styling
│   ├── my_ideas.css                # Styling for My Ideas page
│   └── 1.jpg                       # Background image
│
├── templates/                      # HTML templates
│   ├── index.html                  # Home/Login/Register page
│   ├── idea.html                   # Submit idea page
│   ├── my_ideas.html               # User's ideas page
│   ├── admin_dashboard.html        # Admin dashboard
│   └── aboutus.html                # About Us page
│
└── db/                             # (Optional) SQL scripts, backups
    └── schema.sql                  # SQL Server schema and seed data
```

**Tech Stack / Technologies Used**
- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- Database: SQL Server 2019
- Libraries: pyodbc, hashlib, datetime
- Tools: VS Code, SQL Server Management Studio

**Installation & Setup**
```

Step 1: Clone the repository
git clone https://github.com/your-username/online-idea-box.git
cd online-idea-box

Step 2: Create virtual environment 
python -m venv venv
venv\Scripts\activate     # For Windows
or
source venv/bin/activate  # For Mac/Linux

Step 3: Install required packages
pip install -r requirements.txt

Step 4: Configure database connection
 conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-56E9GOD\\SQLEXPRESS;'
    'DATABASE=IdeaBoxDB;'
    'UID=sa;PWD=rns11;'
    'TrustServerCertificate=yes;'
)

Step 5: Run the Flask application
python app.py
```


###  Future Enhancements

* **Email Notifications**: Notify users and admins via email when a new idea is submitted or replied to.
* **File Upload Support**: Allow users to attach screenshots or documents to their idea submissions.
* **Search & Filter**: Add advanced search and multi-filter options (by user, date, keywords).
* **Admin Analytics Dashboard**: Show charts for idea trends, user participation, and status distributions.
* **Comment Threading**: Allow follow-up comments between users and admins on each idea.
* **User Profiles**: Enable users to view and update their profile, see all their past submissions and replies.

 ## **Conclusion**
The Online Idea Box project offers a simple and user-friendly platform for students and faculty to submit their ideas and feedback, while enabling admins to review and respond effectively. Built with Flask and SQL Server, it demonstrates practical skills in web development, database integration, and user role management. This system fosters transparent communication and encourages innovation within educational institutions.


