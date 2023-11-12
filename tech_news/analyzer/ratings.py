from tech_news.database import find_news
from collections import OrderedDict, Counter


# Requisito 10
def top_5_categories():
    """A função deve buscar as categorias do banco de dados e
    calcular a sua "popularidade" com base no número de ocorrências
    Em caso de empate, o desempate deve ser por ordem alfabética
    de categoria"""
    all_news = find_news()
    list_categories = [new["category"] for new in all_news]
    # ordena a lista por ocorrências em ordem decrescente e,
    # se houver empate, por ordem alfabética
    count_elements = Counter(list_categories)
    list_ordered = sorted(
        list_categories,
        key=lambda x: (-count_elements[x], x))
    # remove os elementos repetidos da lista
    non_repeat_list = list(OrderedDict.fromkeys(list_ordered))
    return non_repeat_list[0:5]


if __name__ == "__main__":
    print(top_5_categories())
