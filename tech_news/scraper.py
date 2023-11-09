import requests
import time
# from bs4 import BeautifulSoup


# Requisito 1
def fetch(url: str):
    """Seu código deve vir aqui"""
    # respeita um rate limit de 1 segundo entre as requisições
    time.sleep(1)
    try:
        # requisição abandonada após 3 segundos sem resposta
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"})
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError


if __name__ == "__main__":
    url = "https://www.tecmundo.com.br/novidades"
    html = fetch(url)
    print(html)
