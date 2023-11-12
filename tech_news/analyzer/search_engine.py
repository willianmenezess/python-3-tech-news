from tech_news.database import db, search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    """Recebe o título da notícia como parametro e retorna
    uma lista de tuplas com as notícias encontradas no DB."""
    searched_news = list(
        db.news.find(
            # $options é usado para fornecer opções à expressão regular regex
            # i é para case insensitive
            {"title": {"$regex": title, "$options": "i"}},
            {"title": 1, "url": 1, "_id": 0},
        )
    )
    return [(news["title"], news["url"]) for news in searched_news]


def is_valid_date_format(date, date_format):
    try:
        # Tenta converter a string para um objeto datetime
        datetime.strptime(date, date_format)
        return True
    except ValueError:
        # Se ocorrer um erro, a string não está no formato desejado
        return False


# Requisito 8
def search_by_date(date):
    """Recebe a data no formato "yyyy-mm-dd" e retorna uma lista de tuplas"""
    date_format = "%Y-%m-%d"
    if is_valid_date_format(date, date_format) is False:
        raise ValueError("Data inválida")
    # invertendo a data para o formato dd/mm/yyyy
    new_date = datetime.strptime(date, date_format).strftime("%d/%m/%Y")
    query = {"timestamp": {"$regex": new_date}}
    searched_news = search_news(query)
    return [(news["title"], news["url"]) for news in searched_news]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    query = {"category": {"$regex": category, "$options": "i"}}
    searched_news = search_news(query)
    return [(news["title"], news["url"]) for news in searched_news]


if __name__ == "__main__":
    # print(search_by_date("2018-11-21"))
    print(search_by_category("Ferramentas"))
