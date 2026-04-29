# Estudo de Web Scraping

Este repositório contém meus estudos, experimentos e projetos práticos focados em Web Scraping utilizando o framework Scrapy em Python. O objetivo é consolidar o conhecimento sobre extração, tratamento e armazenamento de dados provenientes da web.

## Estrutura do Repositório

**/01course-scrapeops**: Contém os códigos desenvolvidos a partir da playlist
[The Python Scrapy Playbook](https://www.youtube.com/watch?v=NkIlpHTFCIE&list=PLkhQp3-EGsIi39YF-BE306DDX1xVSTHmn&index=1) do canal ScrapeOps.

**/02course-walisson-silva**: Contém os códigos desenvolvidos a partir da playlist
[Web Scraping com Python](https://www.youtube.com/watch?v=42sTntMEn6o&list=PLg3ZPsW_sghSkRacynznQeEs-vminyTQk) do canal Walisson Silva.

## Como executar os projetos

Crie e ative um ambiente virtual:

```
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

Instale as dependências:
```
pip install scrapy
```

Navegue até a pasta da spider desejada e execute:

```
scrapy crawl nome_da_spider
```
