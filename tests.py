from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

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
        assert collector.get_book_genre('Каспер') == 'Фантастика'  # Проверяем, что жанр установлен

# 3 Проверяем get_books_with_specific_genre— выводит список книг с определённым жанром.
    def test_get_books_with_specific_genre_assigned_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Каспер')
        collector.set_book_genre('Каспер', 'Фантастика')
        collector.add_new_book('Зомби')
        collector.set_book_genre('Зомби', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Каспер']  # Проверяем жанр

# 4 Проверяем get_books_for_children — возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Смешарики')
        collector.set_book_genre('Смешарики', 'Мультфильмы')
        collector.add_new_book('Мультфильмы')
        collector.set_book_genre('Мультфильмы', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Смешарики']  # Проверяем, что книга для детей возвращается

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

# 9 тестирование количества книг в избранных после добавления нескольких книг
    @pytest.mark.parametrize(
    'name, book_count',
    [
        (['Гордость и предубеждение'], 1),
        (['Гордость и предубеждение', 'Что делать, если ваш кот хочет вас убить'], 2),
        ([], 0)
    ]
)
    def test_add_book_in_favorites_quantity_true(self, book, name, book_count):
        for book_name in name:
            book.add_book_in_favorites(book_name)
        favorites = book.get_favorites_books()
        assert len(favorites) == book_count
