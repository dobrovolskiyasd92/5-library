import sys

class LibraryError(Exception):
    pass

class FilterError(LibraryError):
    pass

class CommandError(LibraryError):
    pass

class SortParameterError(LibraryError):
    pass

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
        raise SortParameterError('Неверный параметр сортировки')






def main(act, val):
    match act:

        case 'filter':
            print(filter_books(books, val))

        case 'sort':
            print(sort_books(books, val))

        case _:
            raise CommandError('Неизвестная команда')


try:
    if len(sys.argv) < 3:
        action = sys.argv[1] if len(sys.argv) > 1 else None
        if action == 'filter':
            raise FilterError('Не передан тект фильтра')



    main(sys.argv[1], sys.argv[2])

except (FilterError, SortParameterError, CommandError) as e:
    print(f'Error: {e}')

except Exception as e:
    print(f'Unknown Error: {e}')

