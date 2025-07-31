### 📖 Project Description

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

Dark themed UI with responsive design
**Tech Stack / Technologies Used**
- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- Database: SQL Server 2019
- Libraries: pyodbc, hashlib, datetime
- Tools: VS Code, SQL Server Management Studio

**Installation & Setup**
Step 1: Clone the repository
git clone https://github.com/your-username/online-idea-box.git
cd online-idea-box

Step 2: Create virtual environment (optional but recommended)
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

