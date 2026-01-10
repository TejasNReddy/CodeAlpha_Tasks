# CodeAlpha – Task 3: Secure Coding Review

## 📌 Project Overview
This project demonstrates a secure coding review of a Python Flask authentication system. It includes both an intentionally vulnerable implementation and a secure implementation, showing how common security flaws can be identified and fixed using industry best practices.

The primary focus is on:
- SQL Injection prevention
- Secure password handling
- Safe application configuration

---

## 🎯 Objective
To analyze an insecure authentication module, identify vulnerabilities, and remediate them by applying secure coding principles aligned with OWASP Top 10 recommendations.

---

## 🛠️ Technology Stack
- Programming Language: Python
- Web Framework: Flask
- Database: SQLite
- Security Library: Werkzeug

---

## 📁 Project Structure
```
CodeAlpha_Secure-Coding-Review/
│
├── app.py                  # Secure implementation (final version)
├── insecure.py             # Intentionally vulnerable version
├── init_db.py              # Initializes secure database (hashed passwords)
├── init_insecure_db.py     # Initializes insecure database (plaintext passwords)
├── SECURITY_REVIEW.md      # Detailed secure coding review report
└── README.md               # Project documentation
```

---

## 🚨 Identified Vulnerabilities (Insecure Version)

1. SQL Injection  
   - Dynamic SQL queries built using user input.
   - Allows attackers to bypass authentication.

2. Insecure Password Storage  
   - Passwords stored in plain text.
   - High risk if database is compromised.

3. Debug Mode Enabled  
   - Exposes internal application details.

---

## 🔐 Secure Coding Fixes Implemented

1. Parameterized Queries  
   - Prevents SQL Injection by separating data from SQL logic.

2. Adaptive Password Hashing  
   - Passwords are hashed using Werkzeug’s scrypt algorithm.
   - Includes salting and key stretching.

3. Secure Authentication Flow  
   - Password verification handled using check_password_hash().

4. Production-Safe Configuration  
   - Flask debug mode disabled.

---

## ▶️ How to Run the Project

### Demonstrate Vulnerable Version
```
python init_insecure_db.py
python insecure.py
```

Test using Postman:
- Method: POST
- URL: http://127.0.0.1:5000/login
- Body: x-www-form-urlencoded

Example:
```
username = admin' --
password = anything
```

---

### Demonstrate Secure Version
```
python init_db.py
python app.py
```

Valid login:
```
username = testuser
password = testpass
```

SQL Injection attempts now fail.

---

## 📄 Documentation
Detailed vulnerability analysis and remediation steps are available in SECURITY_REVIEW.md.

---

## ✅ Conclusion
This project demonstrates how insecure authentication mechanisms can be exploited and how applying secure coding practices—such as parameterized queries and adaptive password hashing—can effectively mitigate these risks.

---

## 👤 Author
Tejas N Reddy  
CodeAlpha Internship – Secure Coding Review (Task 3)
