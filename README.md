# 🔐 Cybersecurity Authentication Toolkit

## 📌 Project Description

Cybersecurity Authentication Toolkit is a web-based authentication system developed using Python and Flask.

The project demonstrates secure authentication concepts such as user registration, password validation, password strength checking, secure password hashing, login authentication, session management, and logout.

## 🎯 Objective

The main objective of this project is to demonstrate how secure authentication can be implemented in a web application.

## ✨ Features

- User Registration
- User Login
- Password Strength Validation
- Password Confirmation
- Secure Password Hashing
- User Authentication
- Session Management
- Protected Dashboard
- Logout
- Duplicate Email Detection
- Invalid Login Handling
- Input Validation

## 🛠️ Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Werkzeug

## 🔒 Security Features

### Password Strength

The application checks that passwords contain:

- At least 8 characters
- Uppercase letter
- Lowercase letter
- Number
- Special character

### Password Hashing

Passwords are not stored as plain text.

The application uses password hashing before storing passwords in the database.

### Authentication

During login, the entered password is checked against the stored password hash.

### Session Management

A session is created after successful login and cleared when the user logs out.

### Protected Dashboard

Only authenticated users can access the dashboard.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK