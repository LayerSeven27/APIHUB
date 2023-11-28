import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

# Guardar el HTML en un archivo
with open(fr"{directorio_destino}/pagina.html", "w", encoding="utf-8") as file:
    file.write(html)
