books = {
    'Война и Мир': 'Толстой Л. Н.',
    '1984': 'Оруэлл Д.',
    'Три мушкетера': 'Дюма',
    'Графиня де Монсоро': 'Дюма',
    'Сорок пять': 'Дюма',
    'Ведьмак': 'Сапковский А.',
    'Сага о Рейневане': 'Сапковский А.'
}


def print_library(library):
    authors = set()
    for value in library.values():
        authors.add(value)
    return sorted(authors)

title_books = list(map(lambda title: title, books.keys()))

print(print_library(books))
print(title_books)