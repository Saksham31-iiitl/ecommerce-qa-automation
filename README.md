# E-Commerce Website Functional Testing Automation

This project automates the functional testing of a demo e-commerce website (e.g., OpenCart) using **Selenium WebDriver** and **Python**.  
The automation suite covers **login, product search, add-to-cart, cart management, and checkout flows**, as well as negative test scenarios.

---

## **Features**

- Page Object Model (POM) for clean, maintainable test code
- Pytest-based, modular test structure
- Configurable with your own test credentials and base URL
- Explicit waits for reliable web interaction
- Easy-to-extend utilities (`helpers.py`)

---

## **Project Structure**

ecommerce-qa-automation/
│
├── config/
│ └── config.yaml # Test config (base URL, credentials)
├── pages/
│ ├── base_page.py # (optional, shared base for POM)
│ ├── login_page.py
│ ├── search_page.py
│ ├── product_page.py
│ ├── cart_page.py
│ └── checkout_page.py
├── tests/
│ ├── test_login.py
│ ├── test_search.py
│ ├── test_add_to_cart.py
│ ├── test_cart.py
│ ├── test_checkout.py
│ └── test_negative_flows.py
├── utils/
│ └── helpers.py
├── conftest.py # Pytest fixtures
├── requirements.txt
└── README.md


---

## **Setup Instructions**

1. **Clone the Repository**

    ```bash
    git clone <your-repo-url>
    cd ecommerce-qa-automation
    ```

2. **Create a Virtual Environment (optional but recommended)**

    ```bash
    python -m venv venv
    # Activate:
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Edit Configuration**

    - Fill `config/config.yaml` with your local e-commerce site URL and credentials:
      ```yaml
      base_url: "http://localhost:8080"
      username: "your_email_or_username"
      password: "your_password"
      ```

5. **Run the Tests**

    ```bash
    pytest
    ```
    Or run an individual test:
    ```bash
    pytest tests/test_login.py
    ```

---

## **Notes**

- This suite is designed to run against a **local or Dockerized instance of OpenCart** (recommended to avoid CAPTCHAs/bot detection).
- All test credentials are configurable in `config/config.yaml`.
- You can add more tests easily using the Page Objects and utilities provided.

---

## **Key Files**

| File/Folder       | Purpose                                   |
|-------------------|-------------------------------------------|
| `pages/`          | Page Object Model classes for site pages  |
| `tests/`          | All functional and negative test scripts  |
| `utils/helpers.py`| Utility functions for waits, screenshots, etc. |
| `config/config.yaml` | Test configuration                     |
| `conftest.py`     | Global pytest fixtures                    |

