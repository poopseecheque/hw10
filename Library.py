class Book:
    def __init__(self, title, author, year, price, country, stoplist=False):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.stoplist = stoplist
        self.country = country
    
    
    def get_info(self):
        if self.stoplist == True:
            status = "on stoplist"
        else:
            status = "not on stoplist"
        print(f"Author: {self.author}, Title: {self.title}, Year: {self.year}, Price: {self.price}, Stoplist: {status}")

    def most_exp(list_of_books):
        most_expensive_book = list_of_books[0]
        max_price = list_of_books[0].price
        for book in list_of_books:
            price = book.price
            if price > max_price:
                max_price = price
                most_expensive_book = book
        return most_expensive_book
    
    def set_stoplist(self, status):
        self.stoplist = status
        
    def censor(self, author_name, status):
        if self.author == author_name:
            self.set_stoplist(status) 