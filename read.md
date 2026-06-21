# 🚀 Selenium Python Framework - Interview Notes

## 🎯 Introduction

“I have built a Selenium automation framework using Python, PyTest, and Page Object Model. It is designed to be scalable, maintainable, and reusable.”

---

# 🏗️ Framework Architecture
Test → BaseClass → Page Objects → Selenium → Browser
↑
conftest (fixture



project/
│
├── tests/ # Test cases
├── pages/ # Page Object Model
├── utils/ # BaseClass & utilities
├── conftest.py # Fixtures





---

# ✅ 1. Tests Layer (`tests/`)

- Contains test cases only
- Includes assertions
- No Selenium logic

### Example:
```python
def test_register_user(self):
    assert account.verify_account_created()


✅ 2. Page Object Model (pages/)
Each page = separate class
Contains locators + methods
Example:
def click_signup(self):
    self.driver.find_element(*self.signup_btn).click()

👉 Interview Line:

“I used Page Object Model to separate UI logic from test logic.”

✅ 3. BaseClass (utils/)
Contains reusable methods
Logging
Explicit waits
Example:
def wait_for_element(self, locator):

👉 Interview Line:

“BaseClass contains reusable utilities like explicit waits and logging.”

✅ 4. conftest.py (Fixtures)
Handles setup & teardown
Centralized driver initialization
Example:
@pytest.fixture(scope="class")
def setup(request):

👉 Interview Line:

“I use conftest.py to centralize driver setup using PyTest fixtures.”

⚙️ Fixtures (Important)
Used for setup and teardown
Avoids code duplication
Key Points:
scope="class" → runs once per class
yield → separates setup and teardown

👉 Interview Answer:

“Fixture is used for setup and teardown. I use class-scoped fixture to initialize the browser once and quit after execution.”

🧠 OOP Concepts Used
✅ Inheritance
class TestRegisterUser(BaseClass):

👉 “Used to reuse common methods”

✅ Encapsulation
Page classes hide locators and actions

👉 “Page objects encapsulate web elements and actions.”

✅ Abstraction
account.create_account_btn()

👉 “Test layer is abstracted from Selenium implementation.”

⏱️ Wait Strategy
Using Explicit Wait instead of time.sleep
Example:
self.wait_for_element(locator)

👉 Interview:

“Explicit waits improve stability and handle dynamic elements.”

🔁 Test Data Handling
Dynamic email generation
Example:
def generate_email():

👉 Interview:

“I generate dynamic test data to avoid duplicate issues.”

🔽 Dropdown Handling
Using Select class
Example:
Select(element).select_by_visible_text("India")

👉 Interview:

“I use Select class to handle dropdowns.”
