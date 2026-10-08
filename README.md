# 🔐 Cybersecurity Authentication Toolkit

**Name:** M. Sirivally  
**Roll Number:** 24071A05R1  



**Live/Demo Link:**  
https://cybersecurity-authentication-toolkit.onrender.com/

---

## 📌 Project Description

The Cybersecurity Authentication Toolkit is a web-based authentication application developed using Python and Flask. It demonstrates important cybersecurity concepts such as secure user registration, password validation, password strength checking, password hashing, user authentication, session management, and logout.

The project is designed to show how authentication can be implemented securely in a web application.

## 🎯 Objective

To develop a secure authentication system that protects user credentials and demonstrates basic cybersecurity controls.

## ✨ Features

- User Registration
- User Login
- Password Strength Checking
- Password Validation
- Secure Password Hashing
- User Authentication
- Session Management
- Protected Dashboard
- Logout
- Email Validation
- Duplicate Account Detection
- Invalid Login Handling

## 🛠️ Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Werkzeug

## 🔒 Security Features

### Password Strength Checking

The application checks that passwords contain:

- At least 8 characters
- Uppercase letter
- Lowercase letter
- Number
- Special character

### Password Hashing

Passwords are never stored as plain text. They are converted into secure password hashes before being stored in the database.

### Authentication

During login, the entered password is verified against the stored password hash.

### Session Management

A session is created after successful login and cleared when the user logs out.

### Protected Dashboard

Only authenticated users can access the dashboard.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/sirivally574/cybersecurity-authentication-toolkit.git
