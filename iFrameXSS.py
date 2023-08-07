from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace 'your_web_app_url' with the URL of your test web application
url = 'http://localhost/FYP/details.php?asset_id=6'
login_url = 'http://localhost/FYP/login.php'
username = '123'
password = '123'

# Define XSS payloads to test (e.g., simple alert scripts)
xss_payloads = [
    "<script>alert('XSS test');</script>",
    "<img src='x' onerror=alert('XSS test')>",
    # Add more payloads to test
]

# Create a WebDriver instance (e.g., ChromeDriver or FirefoxDriver)
driver = webdriver.Firefox()  # Change to Firefox if you prefer

try:
    # Step 1: Login to the application
    driver.get(login_url)

    # Locate and fill in the login form with your credentials
    username_input = driver.find_element(By.NAME, "idusername")
    password_input = driver.find_element(By.NAME, "idpassword")
    login_button = driver.find_element(By.ID, "login")

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()

    # Wait for login to complete (adjust as needed)
    time.sleep(3)

    # Step 2: Access the page with the iframe
    driver.get(url)

    for payload in xss_payloads:
        # Step 3: Locate the iframe element
        iframe = driver.find_element(By.CLASS_NAME, "iframe")

        # Inject the payload into the iframe source attribute
        driver.execute_script(f"arguments[0].src = '{payload}'", iframe)

        # Wait for a few seconds (adjust as needed) to see if the XSS payload is executed
        time.sleep(5)

        # Check if the XSS payload has been executed within the iframe
        # You can use other methods to check for successful XSS execution based on your web application's behavior

finally:
    driver.quit()
