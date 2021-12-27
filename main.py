from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

#Type your Linkedin login informations here.
ACCOUNT_EMAIL = "YOUR LOGIN EMAIL ADDRESS"
ACCOUNT_PASSWORD = "YOUR PASSWORD"
PHONE_NUMBER = "YOUR PHONE NUMBER"

#Change drive path area with yours path
chrome_driver_path = "YOUR DRIVER PATH"
driver = webdriver.Chrome(chrome_driver_path)


driver.get("https://www.linkedin.com/jobs/search/")

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)