from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# estou usando firefox, mas você pode usar outro navegador, como Chrome ou Edge, basta instalar o driver correspondente e ajustar a linha de inicialização do driver abaixo.
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    # 1. Abre o Google
    driver.get("https://www.google.com")

    # 2. Localiza o input de pesquisa
    campo_pesquisa = driver.find_element(By.NAME, "q")

    # 3. Digita o texto e aperta Enter
    campo_pesquisa.send_keys("Curso de Scrapy Python")
    campo_pesquisa.send_keys(Keys.ENTER)

    # 4. Espera alguns segundos para você ver o resultado
    time.sleep(5)
    
    print("Pesquisa realizada com sucesso!")
    print(f"Título da página de resultados: {driver.title}")

finally:
    driver.quit()