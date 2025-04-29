 ##Project Requirements:

 
Functional Requirements
User Authentication

Users must log in using their name and account number.

Password length must be a minimum of 8 characters.

Login validates against data in the CLIENTS or TEMP tables.

User Registration

Two modes of registration:

Using ATM card details (with full KYC).

Using temporary account with CVV (without KYC).

Fields required: Account Number, DOB, Mobile Number, Aadhar Number, CVV, and Name.

Captcha-style human verification code implemented before submission.

User Dashboard

Displays current account balance (randomized for simulation).

Option to make a payment:

Inputs: Amount, recipient account number, and payment reason.

Confirmation via popup message.

ATM Registration (TEMP table)

Users can register with temporary account and CVV.

Display KYC reminder upon accessing payment functionality.

Forgot Password

Users are directed to contact support via a phone number.

Security Tips

A separate alert window advises users on avoiding phishing and fraud.

🧰 Technical Requirements
Python Libraries:

tkinter (GUI)

ttk (Themed widgets)

PIL.ImageTk and PIL.Image (Image handling)

random (Generating dummy balances and verification codes)

mysql.connector (MySQL database connection)

Database:

MySQL Server with:

BANK database.

CLIENTS table: stores full account registration.

TEMP table: stores temporary ATM-based registration.

Assets:

Various .gif and .jpg image files for GUI icons and backgrounds.

File paths are hardcoded (e.g., D:\\gif\\...), which need adjustment for deployment
