from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

# Path to geckodriver is expected to be in PATH

driver = webdriver.Firefox()  # Visible browser

try:
    driver.get("http://localhost:3000")  # Change to deployed URL if needed
    time.sleep(5)

    # --- You will add sign up, course creation, etc. steps here ---

finally:
    time.sleep(5)
    driver.quit()
