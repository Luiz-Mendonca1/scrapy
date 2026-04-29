# ==============================================================================
# 1. Abra o terminal na pasta principal do seu repositório (pasta 'scrapy').
# 2. Certifique-se de que o seu ambiente virtual (venv) está ativo.
# 3. Execute o script utilizando o comando abaixo:
#
#    python 02course-walisson-silva/requisicoes.py
#
# Dica: Use 'python' ou 'python3' dependendo da sua configuração de sistema.
# ==============================================================================

import requests

# Realiza a requisição GET para o site alvo
response = requests.get('https://www.walissonsilva.com/')

# Exibe o código de status da resposta (ex: 200 para sucesso)
print('Status code:', response.status_code)

# Exibe os headers da resposta HTTP
print('↓↓ Header ↓↓')
print(response.headers)

# Exibe o conteúdo HTML da página como texto
print('\n↓↓ Content ↓↓')
print(response.text)