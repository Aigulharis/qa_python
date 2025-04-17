import pytest

from helpers import generate_random_collector_name
from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def collector_with_favorite(collector):
    random_name = generate_random_collector_name()
    collector.add_book_in_favorites(random_name)
    return collector
