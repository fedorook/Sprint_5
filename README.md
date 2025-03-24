🧪 Sprint 5 – Autotests for Stellar Burgers
This project is part of the [Yandex Practicum] QA Engineer course (Sprint 5). It contains automated UI tests for the Stellar Burgers web application — a fictional burger constructor platform built with React.

✅ Project Goals
Write functional UI tests using Selenium WebDriver to verify key features of the Stellar Burgers platform:
Registration
Login
Navigation between pages and sections
Logout
Constructor section switching (Buns, Sauces, Fillings)

🧰 Stack
Python 3.13
Selenium
PyTest
ChromeDriver
WebDriverWait (no sleep() used)

🗂 Project Structure
Sprint_5/
├── .idea/                       # IDE settings (ignored via .gitignore)
├── .venv/                       # Virtual environment (ignored)
├── src/
│   ├── config.py                # Base URLs and configs
│   ├── locators.py              # All page element locators
│   └── utils.py                 # Common helpers like login, email generator, login check
├── tests/
│   ├── test_constructor_sections.py  # Constructor tabs test
│   ├── test_login.py                # All login scenarios
│   ├── test_logout.py               # Logout from profile
│   ├── test_navigation.py           # Navigation between pages
│   ├── test_registration.py         # Registration flow
│   └── conftest.py                  # PyTest fixtures (driver setup/teardown)
├── .gitignore
└── README.md                    # This file

🔍 What Is Tested
🧑‍🚀 Registration
✅ Successful registration with valid inputs
✅ Error message for password shorter than 6 characters

🔐 Login
✅ Via “Войти в аккаунт” on main page
✅ Via “Личный кабинет”
✅ From registration page
✅ From password recovery page

🔄 Navigation
✅ From main to profile (“Личный кабинет”)
✅ From profile to constructor via “Конструктор” and the Stellar Burgers logo

🚪 Logout
✅ Logging out via “Выйти” in profile

🍔 Constructor Section
✅ Switching between “Булки”, “Соусы”, and “Начинки”

🧪 How to Run
Make sure you have Python, Chrome, and ChromeDriver installed and accessible via PATH.

Create and activate virtualenv:
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

Install dependencies:
pip install -r requirements.txt

Run all tests:
pytest tests/

Or run a specific test:
pytest tests/test_login.py

📌 Notes
Unique emails are generated automatically using the format sergeifedoruk19XYZ@ya.ru (where XYZ is a random 3-digit number).
All tests open a fresh browser session and close it after completion.
No time.sleep() — smart WebDriverWait is used for synchronization.

👨‍🚀 Author
Sergei Fedoruk