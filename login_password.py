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
    driver.get("https://the-internet.herokuapp.com/login")

    time.sleep(1)

    user = driver.find_element(By.ID, "username")
    user.send_keys("Tomsmith")

    password = driver.find_element(By.ID,"password")
    password.send_keys("SuperSecretPassword!")

    boton_login = driver.find_element(By.CLASS_NAME,"radius")
    boton_login.click()

    mensaje = driver.find_element(By.ID,"flash").text
    if "You logged into a secure area!" in mensaje:
      print("Login exitoso")
    else:
        print("Login fallido")
    
    time.sleep(5)

finally:

    driver.quit()
    
