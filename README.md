# SkillSync – AI-Powered Skill Tracker Web Application

SkillSync is a personal skill management and course tracking web application designed to help users monitor their learning progress and manage their skill development. Built with Django and integrated with Bootstrap, it offers a seamless interface for adding skills, enrolling in courses, and updating progress dynamically.

---

## 🚀 Features

- 🔐 **User Authentication** – Secure signup, login, and logout system
- 🎯 **Skill Tracking** – Add and view personal skillsets with descriptions
- 📚 **Course Management** – Enroll in external courses with tracking
- 📊 **Progress Monitoring** – Track learning progress with dynamic progress bars
- 📈 **REST API** – API endpoints for skills and courses using Django REST Framework
- 🧠 **Admin Panel** – Manage all data from Django’s built-in admin interface
- 💻 **Responsive UI** – Designed using Bootstrap for mobile-friendly usage

---

## 🛠️ Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (local dev)
- **APIs:** Django REST Framework
- **Version Control:** Git & GitHub

---

## ⚙️ Installation & Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/Pavan14kumar24/skillsync.git
   cd skillsync
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv skillsync_env
   source skillsync_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**
   ```bash
   python manage.py runserver
   ```

7. Visit: `http://127.0.0.1:8000/`

---

## 📸 Screenshots

(Insert screenshots of homepage, login, courses, progress bar here)

---

## 📂 Folder Structure

```
skillsync/
├── core/
│   ├── templates/
│   │   └── core/
│   ├── models.py
│   ├── views.py
│   └── ...
├── static/
│   └── core/
│       └── styles.css
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## 📌 Future Enhancements

- Integrate AI recommendations for courses
- Progress analytics dashboard
- OAuth social logins
- Deployment to cloud (e.g., Render, Heroku)

---

## 👨‍💻 Author

**Pavan Kumar Magubehara**  
Information Technology Major  
[GitHub](https://github.com/Pavan14kumar24)

---

## 📝 License

This project is licensed under the MIT License.
