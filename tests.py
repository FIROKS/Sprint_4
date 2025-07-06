from main import BooksCollector
import pytest


class TestBooksCollector:
    @pytest.mark.parametrize('name', ['A', 
                             'AA',
                             'A' * 39,
                             'A' * 40])
    def test_add_new_book_add_one_book_book_added(self, books_collector, name):
        collector = books_collector

        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['', 'A' * 41,])
    def test_add_new_book_incorrect_length_book_not_added(self, books_collector, name):
        collector = books_collector

        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_existing_genre_genre_is_set(self, books_collector):
        collector = books_collector

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_set_book_genre_non_existing_genre_genre_not_set(self, books_collector):
        collector = books_collector

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Страшилки')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_get_book_genre_with_non_existing_book_return_none(self, books_collector):
        collector = books_collector

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.get_book_genre('Гордость и предубеждение') == None

    def test_get_book_genre_without_genre_return_empty_string(self, books_collector):
        collector = books_collector

        collector.add_new_book('Гордость и предубеждение и зомби')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_get_books_with_specific_genre_existing_genre_show_books_list(self, books_collector):
        collector = books_collector

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')

        collector.add_new_book('Голодный крик')
        collector.set_book_genre('Голодный крик', 'Детективы')

        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_with_specific_genre_non_existing_genre_show_empty_list(self, books_collector):
        collector = books_collector

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')

        assert len(collector.get_books_with_specific_genre('Страшилки')) == 0

    def test_get_books_genre_with_one_book_return_list_with_one_book(self, books_collector):
        collector = books_collector

        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_genre()) == 1

    def test_get_books_genre_with_zero_books_return_empty_list(self, books_collector):
        collector = books_collector

        assert len(collector.get_books_genre()) == 0

    def test_get_books_for_children_without_age_rating_true(self, books_collector):
        collector = books_collector
        books_with_ratign = ['Голодный крик', 'Игра в гляделки']

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Мультфильмы')

        collector.add_new_book('Голодный крик')
        collector.set_book_genre('Голодный крик', 'Детективы')

        collector.add_new_book('Игра в гляделки')
        collector.set_book_genre('Игра в гляделки', 'Ужасы')

        for name in collector.get_books_for_children():
            assert not name in books_with_ratign

    def test_add_book_in_favorites_add_one_book_one_book_added(self, books_collector):
        collector = books_collector

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_already_added_book_book_not_added(self, books_collector):
        collector = books_collector

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_non_existing_book_book_not_added(self, books_collector):
        collector = books_collector

        collector.add_book_in_favorites('Гордость и зомби')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_one_book_book_deleted(self, books_collector):
        collector = books_collector

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_non_existing_book_book_not_deleted(self, books_collector):
        collector = books_collector

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и зомби')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_one_book_book_in_list(self, books_collector):
        collector = books_collector

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 1
