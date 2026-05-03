# Estudo de Web Scraping

Este repositório contém meus estudos, experimentos e projetos práticos focados em Web Scraping utilizando o framework Scrapy em Python. O objetivo é consolidar o conhecimento sobre extração, tratamento e armazenamento de dados provenientes da web.

## Estrutura do Repositório

**/01course-scrapeops**: Contém os códigos desenvolvidos a partir da playlist
[The Python Scrapy Playbook](https://www.youtube.com/watch?v=NkIlpHTFCIE&list=PLkhQp3-EGsIi39YF-BE306DDX1xVSTHmn&index=1) do canal ScrapeOps.

**/02course-walisson-silva**: Contém os códigos desenvolvidos a partir da playlist
[Web Scraping com Python](https://www.youtube.com/watch?v=42sTntMEn6o&list=PLg3ZPsW_sghSkRacynznQeEs-vminyTQk) do canal Walisson Silva.

## Guia de Inicialização Rápida

**Configurar o Ambiente Virtual**

O uso de um ambiente virtual é obrigatório para garantir a integridade das dependências:
```
# Criar o ambiente
python -m venv venv

# Ativar (Windows)
.\venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate
```

**Instalar Dependências**
Instale todos os pacotes necessários de uma vez:
```
pip install scrapy selenium requests beautifulsoup4 pandas webdriver-manager
```

**Execução**
Para projetos baseados em Scrapy:

```
cd 01course-scrapeops
scrapy crawl nome_da_spider
```

Para scripts de Automação/Selenium:
```
python 02course-walisson-silva/nome_do_arquivo
```
