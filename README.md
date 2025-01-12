# Price Tracker Bot 🛒📊

Este repositório contém um bot em Python para monitoramento de preços de produtos em sites, salvando os dados coletados em um arquivo Excel. O bot utiliza Selenium para acessar e extrair informações do site, e automatiza verificações diárias usando a biblioteca `schedule`. 🚀

## Recursos ✨
- Acessa automaticamente um site especificado. 🌐
- Extrai preços à vista e parcelado de um produto. 💰
- Salva os dados em um arquivo Excel (`.xlsx`). 📁
- Cria o arquivo Excel automaticamente, caso ele não exista. 📝
- Verificações agendadas diariamente. ⏰

## Tecnologias Utilizadas 🛠️
- Python 3.8+ 🐍
- Selenium 🌟
- Pandas 🐼
- OpenPyXL 📊
- Schedule 🗓️

## Instalação ⚙️
1. Clone este repositório:
    ```bash
    git clone https://github.com/CauanNeves/monitoramento-preco.git
    cd monitoramento-preco
    ```
2. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```
3. Certifique-se de que o [Google Chrome](https://www.google.com/intl/pt-BR/chrome/) e o [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) estejam instalados e compatíveis com a versão do navegador. 🌍

## Uso 🖥️
1. Execute o script principal:
    ```bash
    python script.py
    ```
2. O programa verificará os preços e salvará as informações em um arquivo Excel chamado `price_gabinete.xlsx` no diretório atual. 📂

## Estrutura do Arquivo Excel 🗂️
O arquivo Excel gerado conterá as seguintes colunas:
- **ID**: Um identificador incremental. 🔢
- **Date**: A data e hora da coleta dos dados. 📅
- **Price in cash**: O preço à vista do produto. 💵
- **Price full**: O preço parcelado do produto. 💳
- **Link**: O link do produto monitorado. 🔗

## Agendamento ⏲️
O bot está configurado para executar a verificação de preços diariamente. Você pode alterar a frequência ajustando o seguinte trecho do código:
```python
schedule.every(1).day.do(main)
```

## Contribuições 🤝
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request. 🛠️


