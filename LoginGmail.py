from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

username = 'tamara.testautomation@gmail.com'
password = 'Tamara@8'

# Set up the ChromeDriver service
chrome_service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service)

try:
    driver.get("https://mail.google.com/")
    driver.maximize_window()

    # Enter username and submit
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId"))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "identifierNext"))).click()

    # Wait for the password field to be visible and interactable
    password_input = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.NAME, "Passwd")))
    password_input.send_keys(password)

    # Click the "Next" button for the password
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "passwordNext"))).click()

    print("Logged in successfully!")

except Exception as e:
    print("An error occurred:", e)

finally:
    sleep(5)
    driver.quit()
