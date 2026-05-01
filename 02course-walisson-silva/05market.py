import requests
from bs4 import BeautifulSoup

url_base = 'https://www.amazon.com/'
termo_busca = input('Digite o produto que deseja pesquisar: ')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
response = requests.get(url_base + 's?k=' + termo_busca, headers=headers)
site = BeautifulSoup(response.text, 'html.parser')

elemento_produto = site.find('div', attrs={'class': 'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20 gsx-ies-anchor'})

print(site.prettify())

#sistema com falha em diversos e commerce virtuais pela protecao antibots, testado: na amazon, mercado livre, shopee, aliexpress.