from tech_news.database import db


# Requisito 7
# Deve retornar uma lista de tuplas como no exemplo abaixo:
# [
#   ("Título1_aqui", "url1_aqui"),
#   ("Título2_aqui", "url2_aqui"),
#   ("Título3_aqui", "url3_aqui"),
# ]
# A busca deve ser case insensitive


def search_by_title(title):
    """Recebe o título da notícia como parametro e retorna
    uma lista de tuplas com as notícias encontradas no DB."""
    searched_news = list(
        db.news.find(
            {"title": {"$regex": title, "$options": "i"}},
            {"title": 1, "url": 1, "_id": 0},
        )
    )
    return [(news["title"], news["url"]) for news in searched_news]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError


if __name__ == "__main__":
    print(search_by_title("Aprenda a usar o Git"))
