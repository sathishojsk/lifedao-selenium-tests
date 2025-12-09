# 🧪 LifeDAO Automation Testing (Selenium + Python + unittest + POM)

This project contains automated UI test cases for **The LifeDAO** application using:

- 🐍 **Python 3**
- 🧪 **unittest (PyUnit)**
- 🌐 **Selenium WebDriver**
- 🧱 **POM – Page Object Model**
- 🧰 **webdriver-manager** (auto handles ChromeDriver)

The test suite includes **Login**, **Logout**, **Signup**, **Invite Code**, and form validation coverage with clean POM structure.

## 📁 Project Structure

```
LifeDAO-Selenium/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── signup_page.py
│   ├── dashboard_page.py
│
├── tests/
│   └── test_auth.py
│
├── requirements.txt
└── README.md
```

## 🚀 Features Covered

### ✅ Login
- Valid login (URL verification)
- Invalid login (error message verification)

### 🔐 Logout
- Click user avatar → Logout
- Verify redirect to login page

### 📝 Signup Flow
- Click “Sign Up” from login page
- Invite code entry → Signup form
- Empty field validation (email, password)
- Password strength rules
- Repeat password validation

### 🔗 Page Navigation
- Login → Sign Up
- Join → Invite Code → Signup Page

## 📦 Installation

### 1. Clone this repository

```bash
git clone https://github.com/YOUR_USERNAME/lifedao-selenium-tests.git
cd lifedao-selenium-tests
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

`requirements.txt` should include:

```
selenium
webdriver-manager
```

## ▶️ Running the Tests

Run all tests:

```bash
python -m unittest discover -v
```

Run a specific test file:

```bash
python -m unittest tests.test_auth -v
```

## 🌐 Update Base URL

In `test_auth.py`, update:

```python
BASE_URL = "https://your-lifedao-domain.com"
```

## 🧱 Page Object Model (POM)

Each UI screen has its own class:

- `LoginPage` → login actions  
- `SignupPage` → invite + signup actions  
- `DashboardPage` → logout actions  
- `BasePage` → shared selenium methods (click, find, send_keys, waits)

This ensures:

- Reusable UI actions  
- Clean test scripts  
- Faster maintenance  

## 🛠️ How to Add New Test Cases

1. Create new POM file in `pages/`  
2. Import it in `test_auth.py`  
3. Add new unittest methods under the test class  

Example:

```python
def test_new_feature(self):
    page = NewFeaturePage(self.driver)
    page.do_something()
    self.assertTrue(...)
```

## 📷 Screenshots on Failure (Optional)

Add this inside your test:

```python
if not result:
    self.driver.save_screenshot("failure.png")
```

## 📤 Pushing Updates to GitHub

```
git add .
git commit -m "Added signup tests"
git push
```

## 🙌 Contributing

Feel free to fork this repository and submit pull requests.

## 📄 License

This project is for educational and testing purposes.
