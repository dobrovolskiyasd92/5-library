import sys

books = {
    'Война и Мир': 'Толстой Л. Н.',
    '1984': 'Оруэлл Д.',
    'Три мушкетера': 'Дюма',
    'Графиня де Монсоро': 'Дюма',
    'Сорок пять': 'Дюма',
    'Ведьмак': 'Сапковский А.',
    'Сага о Рейневане': 'Сапковский А.'
}


# def print_library(library):
#     authors = set()
#     for value in library.values():
#         authors.add(value)
#     return sorted(authors)
#
# title_books = list(map(lambda title: title, books.keys()))
#
# print(print_library(books))
# print(title_books)

def filter_books(library, flt):
    filtered_books = filter(lambda ba: ba[1] == flt, library.items())
    return list(map(lambda kv: f'{kv[0]} - {kv[1]}', filtered_books))



def sort_books(library, sorted_by):
    if sorted_by == 'author':
        sorted_books = sorted(library.items(), key=lambda kv: kv[1])
        return list(map(lambda kv: f'{kv[0]} - {kv[1]}', sorted_books))
    elif sorted_by == 'title':
        sorted_books = sorted(library.items())
        return list(map(lambda kv: f'{kv[0]} - {kv[1]}', sorted_books))
    else:
        return 'Неизвестный фильтр'







def main(arg, val):
    match arg:

        case 'filter':
            print(filter_books(books, val))

        case 'sort':
            print(sort_books(books, val))

        case _:
            print('Неизвестная команда')


main(sys.argv[1], sys.argv[2])

