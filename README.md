# Список тестов  

**test_add_new_book_add_one_book_book_added**  
Книги, с названием допустимой длины добавляются в список книг

**test_add_new_book_incorrect_length_book_not_added**  
Книги, с названием недопустимой длины не добавляются в список книг

**test_set_book_genre_existing_genre_genre_is_set**  
Возможность добавить книге существующий жанр 

**test_set_book_genre_non_existing_genre_genre_not_set**  
Невозможность добавить книге несуществующий жанр 

**test_get_book_genre_with_non_existing_book_return_none**  
Предусмотрена обработка случая, когда запрашивается жанр несуществующей книги

**test_get_book_genre_without_genre_return_empty_string**  
Возвращается пустую строку, если жанр для книги не был задан

**test_get_books_with_specific_genre_existing_genre_show_books_list**  
Возможность получить список книг по указанному жанру

**test_get_books_with_specific_genre_non_existing_genre_show_empty_list**  
Указав несуществующий жанр - возвращает пустой список

**test_get_books_genre_with_one_book_return_list_with_one_book**  
Возможность получить список книг

**test_get_books_genre_with_zero_books_return_empty_list**  
Возвращается пустой список, если ни одной книги не было добавленно 

**test_get_books_for_children_without_age_rating_true**  
Проверяет, что в список детских книг не было добавлено книг с возрастным рейтингом

**test_add_book_in_favorites_add_one_book_one_book_added**  
Возможность добавить книгу в избранное

**test_add_book_in_favorites_already_added_book_book_not_added**  
Невозможно добавить книгу, уже находящуюся в избранном

**test_add_book_in_favorites_non_existing_book_book_not_added**  
Невозможно добавить книгу в избранное, которой нет в списке книг

**test_delete_book_from_favorites_one_book_book_deleted**  
Возможность удалить книгу из избранного

**test_delete_book_from_favorites_non_existing_book_book_not_deleted**  
При удалении несуществующей в избранном книги, список не меняется

**test_get_list_of_favorites_books_one_book_book_in_list**  
Возможность получить список избранного
