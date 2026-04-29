# ScrapeOps - The Python Scrapy Playbook

Este diretório contém o código desenvolvido durante o acompanhamento da playlist 
[The Python Scrapy Playbook](https://www.youtube.com/watch?v=NkIlpHTFCIE&list=PLkhQp3-EGsIi39YF-BE306DDX1xVSTHmn&index=1)  do ScrapeOps.

## Status do Projeto: Interrompido
Motivo: O curso avança para a integração das spiders com serviços de nuvem da AWS (Amazon Web Services) para deploy e execução em escala. Como o foco atual deste repositório é o aprendizado da lógica do framework Scrapy e execução em ambiente local/on-premise, decidi pausar este curso específico para focar em abordagens que não exijam infraestrutura paga ou complexa de nuvem neste momento.

## O que foi explorado até a interrupção:
Arquitetura Scrapy: Entendimento do fluxo de requisição e resposta.

Fake Browser Headers: Configuração de headers para evitar detecção básica.

ScrapeOps Proxy & Monitoring: Integração básica com o SDK do ScrapeOps para monitoramento de spiders.

Seletores Avançados: Uso de CSS e XPath para extração de dados estruturados.

## Como Executar
Certifique-se de estar com o ambiente virtual (venv) ativo

Instale as dependências:
```
pip install scrapy scrapeops-scrapy
```

Execute uma das spiders:
```
scrapy crawl nome_da_sua_spider
```