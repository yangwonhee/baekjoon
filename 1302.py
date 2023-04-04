import sys

n = int(sys.stdin.readline())
books = dict()

for i in range(n):
    book_data = sys.stdin.readline().rstrip()
    books[book_data] = books.get(book_data, 0) + 1

res = sorted(books.items(), key=(lambda x : (-x[1], x[0])))
print(res[0][0])