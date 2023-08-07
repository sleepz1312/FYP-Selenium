from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace 'your_web_app_url' with the URL of your test web application
url = 'http://localhost/FYP/register.php'

# Define XSS payloads to test (e.g., simple alert scripts)
xss_payloads = [
    "<script>alert('XSS test');</script>",
    "<img src='x' onerror=alert('XSS test')>",
    # Add more payloads to test
    "xss_payload_placeholder"
]

# List of valid email addresses to use
valid_emails = ["test@example.com", "user@gmail.com", "attacker@evil.com"]

# Create a WebDriver instance (e.g., ChromeDriver or FirefoxDriver)
driver = webdriver.Firefox()  # Change to Firefox if you prefer

try:
    # Step 1: Navigate to the registration page
    driver.get(url)

    for payload in xss_payloads:
        for email in valid_emails:
            # Step 2: Fill in the registration form with XSS payload and a valid email
            payload_with_email = payload.replace("xss_payload_placeholder", email)
            username_input = driver.find_element(By.NAME, "username")
            name_input = driver.find_element(By.NAME, "name")
            email_input = driver.find_element(By.NAME, "email")
            password_input = driver.find_element(By.NAME, "password")
            register_button = driver.find_element(By.ID, "login")

            # Clear existing values (if any) in the form fields
            username_input.clear()
            name_input.clear()
            email_input.clear()
            password_input.clear()

            # Fill in the form fields with XSS payload and valid email
            username_input.send_keys(payload_with_email)
            name_input.send_keys(payload)
            email_input.send_keys(email)
            password_input.send_keys(payload)

            # Click the register button to submit the form
            register_button.click()

            # Wait for a few seconds (adjust as needed) to see if the XSS payload is executed
            time.sleep(5)

            # Check if the XSS payload is correctly saved in the database or displayed on the page
            # You can use other methods to check for successful XSS execution based on your web application's behavior

finally:
    driver.quit()
