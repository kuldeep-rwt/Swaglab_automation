# Swaglab_automation
This project is a Selenium-based automation test suite for the Swag Labs demo e-commerce website (https://www.saucedemo.com/). Designed for hands-on practice, it covers real-world automation scenarios like login validation, product cart actions, and checkout flows — following best practices in test automation.

# 🧪 SwagLab Selenium Automation

This project automates a complete user flow on [saucedemo.com](https://www.saucedemo.com) using **Selenium WebDriver**, **PyTest**, and **PyTest-HTML** for reporting.

---

## ✅ Features Covered

- Login with valid credentials
- Add product to cart
- Proceed to checkout
- Fill out checkout form
- Complete order
- Generate HTML test report

---

## 📁 Folder Structure

swaglab_automation/
│
├── pages/
│ ├── login_page.py
│ ├── product_page.py
│ ├── cart_page.py
│ └── checkout_page.py
│
├── tests/
│ └── test_checkout_flow.py
│
├── reports/
│ └── report.html ← Generated after running tests
│
├── conftest.py ← Setup for browser driver
├── requirements.txt ← Required libraries
└── pytest.ini ← PyTest config for report

---

## 📦 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/swaglab_automation.git
   cd swaglab_automation

2. Install Dependencies

bash----
pip install -r requirements.txt

To run all tests and generate an HTML report:

bash------
pytest  

This will:

✅ Launch browser

✅ Run the full checkout flow

✅ Generate a test report inside reports/report.html


After running tests, open the HTML file in your browser:

bash----
reports/report.html
You’ll see a clean summary of test results.
