import requests
import time
from bs4 import BeautifulSoup
from typing import List


# Requisito 1
def fetch(url: str):
    """Recebe url e retorna o conteúdo HTML correspondente"""
    # respeita um rate limit de 1 segundo entre as requisições
    time.sleep(1)
    try:
        # requisição abandonada após 3 segundos sem resposta
        # foi passado um header para evitar o erro 403
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"})
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content: str) -> List[str]:
    """retorna uma lista com as URLs das notícias"""
    bs = BeautifulSoup(html_content, "html.parser")

    news_divs = bs.find_all("div", {"class": "entry-thumbnail"})
    result = []
    for new in news_divs:
        new = new.find("a")["href"]
        result.append(new)
    return result


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
    url = "https://blog.betrybe.com"
    html = fetch(url)
    print(scrape_updates(html))
