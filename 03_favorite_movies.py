#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

film_one_letter1 = my_favorite_movies.index('Т')
film_one_last_letter = my_favorite_movies.index(',')
print(my_favorite_movies[film_one_letter1:film_one_last_letter])

film_last_letter1 = my_favorite_movies.index('Н')
film_last_last_letter = len(my_favorite_movies)
print(my_favorite_movies[film_last_letter1:film_last_last_letter])

film_two_letter1 = my_favorite_movies.index('П')
film_two_last_letter = my_favorite_movies.index(',', film_one_last_letter+1)
print(my_favorite_movies[film_two_letter1:film_two_last_letter])

film2_from_last_letter1 = my_favorite_movies.index('Ч')
film2_from_last_last_letter = my_favorite_movies.index(',', film2_from_last_letter1)
print(my_favorite_movies[film2_from_last_letter1:film2_from_last_last_letter])