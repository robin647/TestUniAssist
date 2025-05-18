from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


Service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=Service)


driver.get("http://localhost:3000/") #website call 

time.sleep(3)
driver.find_element(By.CLASS_NAME, "btn").click()


time.sleep(2)

driver.find_element(By.NAME, "username").send_keys("Testser")
driver.find_element(By.NAME, "email").send_keys("test@example.com")
driver.find_element(By.NAME, "phone").send_keys("01700000000")
time.sleep(1)
driver.find_element(By.NAME, "student_id").send_keys("123456789")
driver.find_element(By.NAME, "password").send_keys("123")

driver.find_element(By.XPATH, "//button[text()='Register']").click()

# Wait to ensure alert comes
time.sleep(3)

try:
    alert = driver.switch_to.alert
    print(" Alert Text:", alert.text)
    alert.accept()
except NoAlertPresentException:
    print("not find")

time.sleep(3)
driver.find_element(By.CLASS_NAME, "logout").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "login").click()

student_id_input = driver.find_element(By.NAME, "student_id")
password_input = driver.find_element(By.NAME, "password")

student_id_input.send_keys("213902105")  # Replace with your test student ID
password_input.send_keys("123")   # Replace with your test password

    # Click the Log In button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

    # Wait for alert or navigation
time.sleep(2)

    # Try to switch to alert
try:
    alert = driver.switch_to.alert
    print(" Alert Text:", alert.text)
    alert.accept()
except:
    print(" No alert popup detected")


time.sleep(3)
reminder_link = driver.find_element(By.ID, "reminderlink")
reminder_link.click()
time.sleep(5)
recommendation_link = driver.find_element(By.ID, "recommendationlink")
recommendation_link.click()
time.sleep(8)
career_link = driver.find_element(By.ID, "career")
career_link.click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "logout").click()   
time.sleep(3)





driver.quit()