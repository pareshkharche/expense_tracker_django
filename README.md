# expense_tracker_django
Expense Tracker
An Expense Tracker web application built using Python, Django, Bootstrap, and SQLite. This project allows users to register, log in, and track their expenses by adding or subtracting amounts as needed.

#screenshots
![1](https://github.com/user-attachments/assets/eef1601d-1035-4449-a2f7-35f56752ac16)
![2](https://github.com/user-attachments/assets/14a50b0c-fd29-4236-aa3b-45e7e9a1c169)
![3](https://github.com/user-attachments/assets/92e9304d-757e-4299-8fb9-6b14cbca869d)
![4](https://github.com/user-attachments/assets/cb161b21-a4bb-413e-9973-e29de2670531)
![5](https://github.com/user-attachments/assets/4e5be9ab-9000-40ef-818b-56b4f973fa10)
![7](https://github.com/user-attachments/assets/7ed4bd15-9095-4437-8dbd-f8b826636696)
![8](https://github.com/user-attachments/assets/8e67e6a9-03be-4730-b04c-231f633e2672)


Features
User Authentication: Register, login, and logout functionality.
Expense Management: Add and subtract expenses to track your financial activity.
Responsive Design: Built using Bootstrap for optimal viewing on various devices.
Lightweight Database: Uses SQLite for easy local setup.
Prerequisites
Ensure you have the following installed before setting up the project:

Python (version 3.8 or higher)
pip (Python package manager)
Virtual environment tool (venv or virtualenv)
Getting Started
Follow these steps to set up and run the project on your local machine:

1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/expense_tracker_django.git
cd expense_tracker_django

2. Create a Virtual Environment
bash
Copy code
# For Linux/Mac
python3 -m venv venv

# For Windows
python -m venv venv
3. Activate the Virtual Environment
bash
Copy code
# For Linux/Mac
source venv/bin/activate

# For Windows
venv\Scripts\activate

4. Install Project Dependencies
bash
Copy code
pip install -r requirements.txt

5. Apply Database Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate

6. Run the Development Server
bash
Copy code
python manage.py runserver

7. Open the Application in Your Browser
Visit: http://127.0.0.1:8000/
