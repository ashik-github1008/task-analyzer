Smart Task Analyzer

A mini-application that helps users prioritize tasks based on due date, importance, effort, and dependencies using a custom scoring algorithm.

The goal is to help you decide what to work on first.

Project Structure:

task-analyzer/
├── backend/                  # Django project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/                    # Django app for tasks
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Task database model
│   ├── scoring.py            # Task scoring algorithm
│   ├── tests.py             
│   ├── urls.py               # App-specific API URLs
│   └── views.py              # API views
├── frontend/                 # Frontend files
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── manage.py
├── db.sqlite3
└── requirements.txt


Setup Instructions

Follow these steps to run the project locally:

1. Clone the repository:

git clone repo-url
cd task-analyzer

2. Create a virtual environment:

Windows:

python -m venv venv
venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Apply database migrations:

python manage.py makemigrations
python manage.py migrate

5. Run the development server:

python manage.py runserver


6. Serve the frontend (optional, using VS Code Live Server):

Open VS Code.

Install the Live Server extension by Ritwick Dey.

Open the frontend folder in VS Code.

Right-click index.html → Open with Live Server.

Frontend will open in your browser (usually http://127.0.0.1:5500/)

7. Test the Application:

Enter tasks in JSON format in the textarea.

Click Analyze to see tasks prioritized dynamically.

[
  {
    "title": "Write report",
    "due_date": "2025-12-05",
    "estimated_hours": 3,
    "importance": 8,
    "dependencies": []
  },
  {
    "title": "Prepare slides",
    "due_date": "2025-12-10",
    "estimated_hours": 5,
    "importance": 6,
    "dependencies": ["Write report"]
  }
]


Scoring Algorithm

The task score is calculated using:

Urgency: Days left until the due date (tasks past due get a penalty).

Importance: Weighted by user-defined importance (1–10).

Effort: Less effort tasks get slightly higher priority.

Dependencies: Tasks that depend on other incomplete tasks get a penalty.

Total score = Urgency + Importance + Effort - Dependency penalty

Tasks are sorted in descending order based on total score.
