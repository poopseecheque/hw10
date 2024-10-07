from Library import Book

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 10.99, "United States", False)
book2 = Book("1984", "George Orwell", 1949, 12.99, "United States", True)
book3 = Book("War and Peace", "Leo Tolstoy", 1869, 18.99, "Russia", False)
book4 = Book("Dune", "Frank Herbert", 1965, 12.99, "United States", False)

booklist = [book1, book2, book3, book4]
    
for book in booklist:
    book.get_info()

most_expensive_book = Book.most_exp(booklist)
print(f"\nThe most expensive book is: {most_expensive_book.title} by {most_expensive_book.author}, price: {most_expensive_book.price}\n")

for book in booklist:
    book.censor("George Orwell", False)
    
for book in booklist:
    book.get_info()