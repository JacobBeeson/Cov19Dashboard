"""tests for the application module"""
from application import time_to_interval
from application import get_covid_data
from application import get_news_articles


def test_time_to_interval():
    assert isinstance(time_to_interval('12:00'), int)


def test_get_covid_data():
    data = get_covid_data()
    assert isinstance(data, dict)


def test_get_news_articles():
    data = get_news_articles()
    assert isinstance(data, list)
    assert isinstance(data[0], dict)
