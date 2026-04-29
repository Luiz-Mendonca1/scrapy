import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')
content = response.text
site = BeautifulSoup(content, 'html.parser')

noticias = site.find_all('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    elemento_titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    
    if elemento_titulo:
        titulo = elemento_titulo.get_text()
        link = elemento_titulo['href']
        
        elemento_subtitulo = noticia.find('a', attrs={'class': 'bstn-relatedtext'}) 
        
        subtitulo = elemento_subtitulo.get_text() if elemento_subtitulo else None

        lista_noticias.append({
            'titulo': titulo,
            'subtitulo': subtitulo,
            'link': link
        })

news = pd.DataFrame(lista_noticias, columns=['titulo', 'subtitulo', 'link'])

news.to_csv('noticias_g1.csv', index=False, encoding='utf-8-sig')

print(news)