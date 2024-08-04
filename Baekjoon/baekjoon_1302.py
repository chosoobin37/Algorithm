num = int(input())
book_sales = {}

for i in range(num):
    book = input().strip()
    if book in book_sales:
        book_sales[book] += 1
    else:
        book_sales[book] = 1
    
most_sold = []
max_sales = 0

for book, sales in book_sales.items():
    if sales > max_sales:
        most_sold = [book]
        max_sales  = sales
    elif sales == max_sales:
        most_sold.append(book)

most_sold.sort()
print(most_sold[0])