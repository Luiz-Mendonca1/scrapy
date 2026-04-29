import requests  # requisitar a página para a internet
from bs4 import BeautifulSoup  # biblioteca ajuda a ler o HTML

response = requests.get('https://g1.globo.com/')

# Pegamos todo o HTML da página em formato string
content = response.text

# BeautifulSoup transforma esse texto confuso em um objeto em mapa
# que o Python consegue entender e pesquisar.
site = BeautifulSoup(content, 'html.parser')

# procuramos a primeira <div> que tenha a classe 'feed-post-body'
noticia = site.find('div', attrs={'class': 'feed-post-body'})

# dentro dessa notícia, procuramos o link (tag <a>) que contém o título
titulo = noticia.find('a', attrs={'class': 'feed-post-link'}).get_text()

print(titulo)