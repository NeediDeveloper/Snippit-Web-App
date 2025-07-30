# 📝 Snippit — Microblogging for Raw Thoughts

Snippit is a minimalist microblogging platform where users can share quick thoughts freely and anonymously. Think of it like Twitter's spiritual cousin — stripped down, raw, and expressive.


---

## 🚀 Features

- ✍️ Create and share bite-sized posts (Snippits)
- 🌊 Beautiful animated SVG banner text
- 🔐 Secure user registration & login system
- 🎨 Dark-mode UI using Tailwind CSS
- ⚙️ Admin panel for post and user management
- 🛡️ Password validation with live feedback

---

## 🛠️ Tech Stack

- **Python 3.13+**
- **Django 5+**
- **SQLite**
- **Tailwind CSS**

---

## 📸 Screenshots
![alt text](<Screenshot.png>)


---

## 🔧 Setup Instructions

1. **Clone this repository**
   git clone https://github.com/YOUR_USERNAME/snippit.git
   cd snippit

2. **Create a Virtual Environmet**
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate


3. **Install requirements**
    pip install -r requirements.txt

4. **Apply migrations**
    python manage.py migrate


5. **Create superuser (for admin access)**
    python manage.py createsuperuser

6. **Run development server**
    python manage.py runserver

7. **Run tailwind server**
    python manage.py talwind start
