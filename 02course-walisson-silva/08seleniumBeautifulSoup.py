# codigo integrando Selenium e BeautifulSoup para extrair dados do Airbnb

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

ff_options = Options()
# ff_options.add_argument('--headless') # Descomente para rodar sem abrir a janela
ff_options.add_argument('--window-size=1200,800')

# 1. Inicialização
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()), 
    options=ff_options
)

try:
    print("Acessando Airbnb...")
    driver.get("https://www.airbnb.com")
    time.sleep(5)

    # 2. Lógica de Pesquisa
    print("Localizando campo de busca...")
    try:
        search_trigger = driver.find_element(By.CSS_SELECTOR, 'button[data-index="0"]')
        search_trigger.click()
        time.sleep(1)
    except:
        pass

    campo_busca = driver.find_element(By.TAG_NAME, "input")
    campo_busca.send_keys("São Paulo")
    campo_busca.send_keys(Keys.ENTER)
    time.sleep(3)

    # 3. Selecionar Hóspedes
    print("Configurando hóspedes...")
    hospedes_btn = driver.find_element(By.XPATH, "//div[text()='Hóspedes'] | //div[text()='Quem']")
    hospedes_btn.click()
    time.sleep(1)

    add_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="stepper-adults-increase-button"]')
    add_button.click()
    time.sleep(0.5)
    add_button.click()
    
    # 4. Clicar no botão de busca
    final_search = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="structured-search-input-search-button"]')
    final_search.click()
    
    print("Aguardando resultados...")
    time.sleep(7) 

    # 5. BeautifulSoup para extração
    page_source = driver.page_source
    site = BeautifulSoup(page_source, 'html.parser')

    cards = site.find_all('div', attrs={'data-testid': 'listing-card-title'})
    
    print(f"\n--- {len(cards)} ACOMODAÇÕES ENCONTRADAS ---")
    for item in cards:
        print(f"Produto: {item.get_text()}")

finally:
    print("\nFim do processo.")
    # driver.quit() # Mantenha comentado se quiser ver o resultado na tela