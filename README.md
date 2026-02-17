# Flask Manager App
A simple Manager Web Application built using Flask.  
This application allows users to register, login, and manage records securely.
# Features
- User Registration
- User Login & Logout
- Session Management
- Dashboard
- Add / Edit / Delete Records
- Flash Messages
- Form Validation
# Tech Stack
- Python 3
- Flask
- HTML5
- CSS3
- Bootstrap
- SQLite (or MySQL)
# Project Structure
flask-manager-app/
├── app.py
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
├── static/
│   ├── css/
│   └── images/
├── requirements.txt
├── README.md
└── .gitignore
# Installation & Setup
1. Clone the repository  
   git clone https://github.com/Vin23820/flask-manager-app.git
2. Navigate into project folder  
   cd flask-manager-app
3. Create virtual environment  
   python -m venv venv
4. Activate virtual environment  
   Windows: venv\Scripts\activate  
   Mac/Linux: source venv/bin/activate  
5. Install dependencies  
   pip install -r requirements.txt
6. Run the application  
   python app.py
7. Open in browser  
   http://127.0.0.1:5000/
# Future Enhancements
- Password Hashing using Werkzeug
- Role-Based Access Control
- Admin Dashboard
- Deployment on AWS / Render
# Author
M.Vinay



