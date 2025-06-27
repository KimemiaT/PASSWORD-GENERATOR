
# 🔐 Password Generator (Django Project)

A simple and modern web-based password generator built using **Django**. Users can customize the length and character types for their password, generate it securely, and copy it to clipboard with one click.

---

## 🚀 Features

- Generate strong passwords
- password strength indicator
- Choose password length
- Include:
  - Uppercase letters
  - Numbers
  - Special characters
- Copy password to clipboard
- Clean, modern UI (Bootstrap 5 + custom styling)

---

## 🛠️ Tech Stack

| Tool           | Purpose                         |
|----------------|----------------------------------|
| **Python 3.12+** | Core programming language        |
| **Django 5.2** | Backend web framework            |
| **HTML/CSS**   | Markup and styling               |
| **Bootstrap 5**| Frontend framework for UI        |
| **JavaScript** | Copy-to-clipboard functionality  |

---

## 🏗️ Folder Structure
password_generator/
├── generator/
│ ├── templates/
│ │ └── generator/
│ │ ├── home.html
│ │ └── password.html
│ ├── views.py
│ ├── urls.py
│ └── ...
├── password_generator/
│ └── settings.py
├── db.sqlite3
├── manage.py
└── README.md

---

## ⚙️ How It Works

1. User selects preferences on the homepage.
2. The backend uses Python's `random` module to generate a secure password.
3. Password is rendered in a new page with an option to copy it.
4. UI is styled using Bootstrap 5 and custom CSS for a modern look.

---

## ▶️ How to Run Locally

```bash
# 1. Clone the repo or create the project manually
git clone <your-repo-url>

# 2. Navigate into the project folder
cd password_generator

# 3. (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate  # For Windows

# 4. Install Django
pip install django

# 5. Run the server
python manage.py runserver

# 6. Open your browser and go to
http://127.0.0.1:8000
