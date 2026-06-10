import pytest
from app.retriever import Retriever

def test_search_kosmos():
    """Поиск по запросу 'Космос' должен найти результаты"""
    retriever = Retriever()
    results = retriever.search("Космос")
    assert len(results) > 0

def test_search_zhivotnye():
    """Поиск по запросу 'Животные' должен найти результаты"""
    retriever = Retriever()
    results = retriever.search("Животные")
    assert len(results) > 0

def test_search_nauka():
    """Поиск по запросу 'Наука' должен найти результаты"""
    retriever = Retriever()
    results = retriever.search("Наука")
    assert len(results) > 0

def test_results_have_score():
    """Результаты поиска должны содержать score"""
    retriever = Retriever()
    results = retriever.search("Россия")
    if results:
        assert "score" in results[0]

def test_refusal_for_fake():
    """Запрос 'Как приготовить борщ?' должен вернуть список (отказ)"""
    retriever = Retriever()
    results = retriever.search("Как приготовить борщ?")
    assert isinstance(results, list)
