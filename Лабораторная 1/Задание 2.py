
information = 1.44 * 1024 * 1024
pages = 100
lines = 50
numbers = 25
symbol = 4

books = information // (pages * lines * numbers * symbol)

print("Количество книг, помещающихся на дискету:", int(books))

