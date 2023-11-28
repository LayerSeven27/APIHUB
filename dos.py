import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor

def ejecutar_script(_):
    # URL de la página web
    url = "http://127.0.0.1:8080"

    # Directorio de destino para guardar el HTML
    directorio_destino = r"tmp"

    # Configuración de Selenium para ejecutar en segundo plano
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecutar en modo sin cabeza

    # Iniciar el navegador
    driver = webdriver.Chrome(options=chrome_options)

    # Esperar 10 segundos para dar tiempo a que se cargue el contenido
    time.sleep(10)

    # Acceder a la página web
    driver.get(url)

    # Esperar a que la página esté completamente cargada
    time.sleep(5)  # Puedes ajustar este tiempo según sea necesario

    # Obtener el HTML de la página
    html = driver.page_source

    # Cerrar el navegador
    driver.quit()

    return html

def ejecutar_multiples_veces(numero_veces, numero_por_vez):
    with ThreadPoolExecutor(max_workers=numero_por_vez) as executor:
        for i in range(numero_veces):
            resultados = list(executor.map(ejecutar_script, range(numero_por_vez)))
            print(f"\nExecuted {numero_por_vez} browser for each {i + 1}\n")

            # Puedes procesar los resultados según sea necesario
            # Por ejemplo, guardar los resultados en archivos HTML, analizarlos, etc.

if __name__ == "__main__":
    # Preguntar al usuario cuántas instancias desea ejecutar cada vez y cuántas veces
    numero_por_vez = int(input("Enter the number of browsers at a time to run: "))
    numero_veces = int(input("Number of times to run: "))

    ejecutar_multiples_veces(numero_veces, numero_por_vez)
