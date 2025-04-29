# 💳 Bharat Bank Online Management System

A desktop GUI application simulating basic banking services like login, registration, and payment. Built with **Python (Tkinter)** and **MySQL**, this project showcases a simplified version of an online banking platform.

---

## 🔖 Features

### User Authentication
- Secure login using account number and username.
- Validation of minimum password length (8 characters).

### User Registration
- Register using:
  - Full KYC (ATM, Aadhar, DOB, Mobile Number, CVV).
  - Temporary registration using ATM and CVV only.
- Captcha-like verification code to confirm human input.

### Dashboard
- Personalized welcome message.
- Displays current balance (randomly generated for simulation).
- Payment form: Amount, account number, reason.

### ATM Registration
- Allows users to register using temporary details.
- Prompts users to complete KYC for full access.

### Additional Functions
- Forgotten password support (help line number).
- Security tips and phishing warnings in a dedicated window.

---

## 🛠️ Technologies Used

- **Language**: Python 3
- **GUI**: Tkinter (including ttk)
- **Database**: MySQL
- **Image Handling**: PIL (Pillow)
- **Others**: Random module (balance simulation, verification codes)

---

## 📂 Database Schema

### CLIENTS Table
| Field       | Type     | Notes                        |
|-------------|----------|------------------------------|
| acc_no      | bigint   | Primary key                  |
| dob         | DATE     | Not null                     |
| mobile_no   | bigint   |                              |
| aadhar_no   | bigint   | Not null                     |
| cvv_no      | bigint   | Unique                       |
| name        | varchar  | Not null                     |

### TEMP Table
| Field     | Type     | Notes       |
|-----------|----------|-------------|
| acc_no    | bigint   | Primary key |
| mobile_no | bigint   |             |
| cvv_no    | bigint   | Unique      |
| name      | varchar  | Not null    |

---

## 🚀 Setup Instructions

### 1. Install Dependencies
```bash
pip install pillow mysql-connector-python
```

### 2. Configure MySQL
- Make sure MySQL is running.
- Modify credentials in the script:
```python
mysql.connector.connect(host='localhost', user='root', password='YOUR_PASSWORD')
```
- On first run, the script automatically creates:
  - `BANK` database
  - `CLIENTS` and `TEMP` tables

### 3. Prepare Assets
- Place all image files (e.g., `.gif`, `.jpg`, `.png`) in the path specified in the script:
```
D:\gif\<image-name>
```
- Adjust image paths in the code if necessary.

### 4. Run the App
```bash
python MEGA\ PROJECT.py
```

---

## ⚠ Warnings

- This application is for **educational/demo purposes only**.
- No real transactions or secure protocols are implemented.
- Passwords are stored in plaintext.
- SQL queries are not parameterized (vulnerable to injection).
- Do **not** use real banking data.

---
