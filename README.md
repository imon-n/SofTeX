
# SofTeX – University/Department Management System

SofTeX is a **Django-based web application** designed to streamline academic and departmental activities.
It centralizes **student, faculty, course, library, and communication management** into one platform,
providing a seamless experience for administrators, teachers, and students.

---

## 🌐 Live Demo

🚀 **[Visit SofTeX Online](https://softex.onrender.com/)**

---

## 🚀 Features

### 📚 Academic Management

* **Courses** – Manage course details, descriptions, and materials
* **Faculty** – Maintain faculty profiles and contact information
* **Alumni** – Showcase alumni details for networking and inspiration

### 📖 Library & Resources

* **Borrow Book** – Track borrowing, returning, and availability of books
* **Documents** – Share and store academic resources & files
* **My Note** – Personal notes section for students/faculty

### 📰 Communication

* **Notice Board** – Post important announcements and updates
* **Media** – Manage and display images or other media files

### 👤 User Management
* Role-based access for **Admin**, **Faculty**, and **Student**
* Secure authentication system with password hashing

---

## 🛠 Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap/Tailwind
* **Database:** SQLite (default) / PostgreSQL (production)
* **Authentication:** Django Auth System
* **Deployment:** Render

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/imon-n/SofTeX.git
   cd SofTeX
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate    # macOS/Linux
   env\Scripts\activate       # Windows
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

5. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

---

## 📂 Project Structure

```
softex/
├── alumni/         # Alumni management
├── borrow_book/    # Library borrow/return system
├── courses/        # Course details and management
├── documents/      # Document storage and sharing
├── faculty/        # Faculty profiles
├── media/          # Uploaded media files
├── my_note/        # Personal notes
├── notice/         # Notice board
├── static/         # Static files (CSS, JS, images)
├── templates/      # HTML templates
├── users/          # Authentication and user management
└── manage.py
```

---

## 👨‍💻 Author

**Md Imon**
🔗 GitHub: [imon-n](https://github.com/imon-n)
🌍 Live: [https://softex.onrender.com/](https://softex.onrender.com/)

---

If you want, I can now **add a “How to Use” section + screenshots from your live site** so it’s more appealing for portfolio and job applications.
Do you want me to add that?
