from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from unittest.mock import patch
import pytest


def test_reading_plan_group_news():
    mock_news = [
        {
            "url": "https://blog.betrybe.com/tecnologia/noticia1",
            "title": "titulo 1",
            "timestamp": "18/05/2023",
            "writer": "Cairo Noleto",
            "reading_time": 7,
            "summary": "primeiro parágrafo da notícia 1",
            "category": "Tecnologia",
        },
        {
            "url": "https://blog.betrybe.com/carreira/noticia2",
            "title": "titulo 2",
            "timestamp": "15/05/2023",
            "writer": "Lucas Custódio",
            "reading_time": 16,
            "summary": "Primeiro parágrafo da notícia 2",
            "category": "Carreira",
        },
    ]

    msg_error = "Valor 'available_time' deve ser maior que zero"
    with pytest.raises(ValueError, match=msg_error):

        ReadingPlanService.group_news_for_available_time(-1)

    with patch(
        "tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy",
        return_value=mock_news,
    ):
        result_method = ReadingPlanService.group_news_for_available_time(7)
        assert len(result_method["readable"]) == 1
        assert len(result_method["unreadable"]) == 1

        assert result_method == {
            "readable": [
                {
                    "unfilled_time": 0,
                    "chosen_news": [("titulo 1", 7)],
                }
            ],
            "unreadable": [("titulo 2", 16)],
        }
