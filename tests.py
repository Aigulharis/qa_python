import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2


# 1 Проверяем словарь books_genre. Одну и ту же книгу можно добавить только один раз
    def test_add_duplicate_book_no_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book('Каспер')
        collector.add_new_book('Каспер')  # Пытаемся добавить дубликат
        assert len(collector.get_books_genre()) == 1  # Проверяем, что книга не добавилась дважды

# 2 Проверяем set_book_genre — присвоение жанра книге
    def test_set_book_genre_has_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Каспер')
        collector.set_book_genre('Каспер', 'Фантастика')
        assert collector.get_book_genre('Каспер') == 'Фантастика'  # Проверяем, что жанр установлен # Проверяем, что жанр установлен

# 2.1 Проверяем get_book_genre— выводит жанр книги по её имени.
    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        expected_genre = 'Фантастика'
        actual_genre = collector.get_book_genre('Дюна')
        assert actual_genre == expected_genre # Проверяем, что жанр книги возвращается по её имени

# 3 Проверяем get_books_with_specific_genre— выводит список книг с определённым жанром.
    def test_get_books_with_specific_genre_assigned_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Каспер')
        collector.set_book_genre('Каспер', 'Фантастика')
        collector.add_new_book('Зомби')
        collector.set_book_genre('Зомби', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Каспер']  # Проверяем жанр

# 4 Проверяем get_books_for_children — возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга
    def test_get_books_for_children_filter_by_age(self):
        collector = BooksCollector()
        collector.add_new_book('Ужас')
        collector.set_book_genre('Ужас', 'Ужасы')
        collector.add_new_book('Смешарики')
        collector.set_book_genre('Смешарики', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Смешарики'] # Проверяем, что книга для детей возвращается

# 5 Проверяем add_book_in_favorites — добавляет книгу в избранное
    def test_add_book_in_favorites_book_add(self):
        collector = BooksCollector()
        collector.add_new_book('Каспер')
        collector.add_book_in_favorites('Каспер')
        assert 'Каспер' in collector.get_list_of_favorites_books()  # Проверяем, что книга добавлена в избранное

# 6 Проверяем delete_book_from_favorites — удаление книги из избранного
    def test_delete_book_from_favorites_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Каспер')
        collector.add_book_in_favorites('Каспер')
        collector.delete_book_from_favorites('Каспер')
        assert 'Каспер' not in collector.get_list_of_favorites_books()  # Проверяем, что книга удалена

# 7 Проверяем delete_book_from_favorites — удаление книги из избранного, если она там есть(удаляем несуществующую книгу из избранного)
    def test_favorites_remains_after_deleting_nonexistent(self):
        collector = BooksCollector()
        collector.add_new_book('Каспер')
        collector.add_book_in_favorites('Каспер')
        collector.delete_book_from_favorites('Неизвестная книга')  # Попытка удалить книгу, которой нет
        assert len(collector.get_list_of_favorites_books()) == 1  # Проверяем, что у нас все еще одна избранная книга

# 8 Проверяем словарь add_book_in_favorites. Повторно добавить книгу в избранное нельзя.
    def test_add_book_in_favorites_duplicate_book_no_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book('Каспер')
        collector.add_book_in_favorites('Каспер')
        collector.add_book_in_favorites('Каспер')  # Пытаемся добавить дубликат
        assert len(collector.get_list_of_favorites_books()) == 1  # Проверяем, что книга не добавилась дважды

#9 тестирование количества книг в избранных после добавления нескольких книг
@pytest.mark.parametrize("book_names,expected_count", [
    ([], 0),  # Без книг
    (["Гордость и предубеждение"], 1),  # 1 книга
    (["Гордость и предубеждение", "Что делать, если ваш кот хочет вас убить"], 2),  # 2 книги
])
def test_add_book_in_favorites_quantity_true(book_names, expected_count):
    collector = BooksCollector()
    for book_name in book_names:
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

    favorite_books = collector.get_list_of_favorites_books()
    assert len(favorite_books) == expected_count
