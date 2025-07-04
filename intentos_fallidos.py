from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

driver = webdriver.Chrome()

    #tomar captura de pantalla
main_folder = "screenshots"

def guardar_captura(numero_prueba, nombre_archivo):

        folder = os.path.join(main_folder, f"Caso_de_Prueba_{numero_prueba}")
        if not os.path.exists(folder):
            os.makedirs(folder) #Crea carpeta con la imagen
        ruta = os.path.join(folder, nombre_archivo)
        driver.save_screenshot(ruta)
        print(f"Captura de pantalla guardada en: {ruta}")

        

try: 


    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)


    # Intento 3 : contraseña incorrecta 3 veces.
    contrasena_incorrecta = ["Prueba12!", "Contraseña123", "12345678"]

    for i,contrasena in enumerate(contrasena_incorrecta,start=1):
      
      username_field = driver.find_element(By.ID, "username")
      password_field = driver.find_element(By.ID, "password")
      Login_button = driver.find_element(By.CLASS_NAME, "radius")
      

      username_field.clear()
      password_field.clear()
      
      time.sleep(2)
      
      username_field.send_keys("tomsmith")
      password_field.send_keys(contrasena)
      Login_button.click()
      
      time.sleep(2)
     
      guardar_captura(1, f"Prueba{i+2}_error_login.png")
    
      time.sleep(3)
     

    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    Login_button = driver.find_element(By.CLASS_NAME, "radius")

# intento 1 : Contraseña incorrecta - Usuario Correcto y Contraseña Incorrecta 

    username_field.send_keys("tomsmith")
    password_field.send_keys("Prueba12!")
    Login_button.click()
    time.sleep(2)
    guardar_captura(2, "Prueba1_error_login.png")
    time.sleep(3)

# Intento 2: Contraseña correcta - Usuario correcto y contraseña correcta

    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    Login_button = driver.find_element(By.CLASS_NAME, "radius")
    username_field.clear()
    password_field.clear()
    time.sleep(2)

    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")
    Login_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "flash")))
    guardar_captura(3, "Login_exitoso.png")
    time.sleep(6)

except Exception as e:
             print("No se pudo encontrar el botón de login. Revisa el sitio web.")

finally:

    time.sleep(10)
    driver.quit()






