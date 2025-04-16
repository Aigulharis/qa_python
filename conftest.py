import pytest

from helpers import generate_random_book_title
from main import BooksCollector


@pytest.fixture(scope="function")
def book():
    book = BooksCollector(name=generate_random_book_title())
    return book

@pytest.fixture()
def book_with_favorite(book):
    book.add_book_in_favorites(generate_random_book_title())
    return book