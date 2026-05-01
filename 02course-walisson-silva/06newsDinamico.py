import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime

# 1. Configurações de diretório e data
pasta_destino = 'dados'
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

data_atual = datetime.now().strftime('%d-%m-%Y')
nome_arquivo = f'noticias_g1_{data_atual}.csv'
caminho_completo = os.path.join(pasta_destino, nome_arquivo)

# 2. Scraping
lista_noticias = []

response = requests.get('https://g1.globo.com/')
content = response.text
site = BeautifulSoup(content, 'html.parser')

noticias = site.find_all('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    elemento_titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    
    if elemento_titulo:
        titulo = elemento_titulo.get_text().strip()
        
        link = elemento_titulo.get('href')
        
        if not link:
            link = "Link não disponível"
        
        elemento_subtitulo = noticia.find('a', attrs={'class': 'bstn-relatedtext'}) 
        subtitulo = elemento_subtitulo.get_text().strip() if elemento_subtitulo else None

        lista_noticias.append({
            'titulo': titulo,
            'subtitulo': subtitulo,
            'link': link
        })

# 3. Exportação com Pandas
news = pd.DataFrame(lista_noticias, columns=['titulo', 'subtitulo', 'link'])

# Salva na pasta 'dados' com o nome dinâmico a data atual
news.to_csv(caminho_completo, index=False, encoding='utf-8-sig')

print(f"Arquivo salvo com sucesso em: {caminho_completo}")
print(news.head())