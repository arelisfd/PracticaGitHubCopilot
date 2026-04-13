from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Opción 1: Con webdriver-manager (más simple)
# pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager


def login_saucedemo(username="standard_user", password="secret_sauce"):
    """
    Realiza login en saucedemo.com
    Usuarios de prueba disponibles:
    - standard_user, locked_out_user, problem_user, performance_glitch_user
    Contraseña: secret_sauce (igual para todos)
    """

    # Iniciar el navegador
    options = webdriver.ChromeOptions()
    # Descomenta la siguiente línea para modo headless (sin interfaz gráfica)
    # options.add_argument("--headless")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        # Navegar a la página
        driver.get("https://www.saucedemo.com/")

        # Esperar a que los elementos carguen
        wait = WebDriverWait(driver, 10)

        # Encontrar y llenar el campo de usuario
        username_field = wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys(username)

        # Encontrar y llenar el campo de contraseña
        password_field = wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(password)

        # Hacer click en el botón LOGIN
        login_button = wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()

        # Esperar a que la página se cargue después del login
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

        print(f"✓ Login exitoso con usuario: {username}")

        # Esperar a que la página esté completamente visible antes de cerrar
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

        return driver

    except Exception as e:
        print(f"✗ Error durante el login: {e}")
        driver.quit()
        return None


# Ejecutar el login
if __name__ == "__main__":
    driver = login_saucedemo()

    # Esperar a que cualquier animación o carga final termine antes de cerrar
    if driver:
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
            )
        except Exception:
            pass
        finally:
            driver.quit()
