from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


try:

    # Abrir el sitio web
    driver.get("https://www.saucedemo.com/")

    time.sleep(1)

    user = driver.find_element(By.ID, "user-name")
    user.send_keys("standard_user")

    password = driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")

    boton_login = driver.find_element(By.ID,"login-button")
    boton_login.click()

    time.sleep(3)

    driver.save_screenshot("screenshots/login_exitoso.png")

    mensaje = driver.find_element(By.ID,"flash").text
    if "You logged into a secure area!" in mensaje:
      print("Login exitoso")
    else:
        print("Login fallido")


    
finally:

    driver.quit()
    
