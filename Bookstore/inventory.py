
import os
import json

FILE_PATH = 'Bookstore/books.json'

class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'price': self.price,
            'stock': self.stock
        }

class Inventory:
    def __init__(self):
        self.books = self.load_books()
    
    def load_books(self):
        if not os.path.exists(FILE_PATH):
            return []
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    
    def save_books(self):
        with open(FILE_PATH, 'w') as fp:
            json.dump(self.books, fp, indent=2)

    def add_to_inventory(self, book: Book):
        book_dict = book.to_dict()
        self.books.append(book_dict)
        self.save_books()
    
    def sell_book(self, title, qty):
        found = False
        for idx, book in enumerate(self.books, 0):
            if book['title'].lower() == title.lower():
                found = True
                if book['stock'] == 0:
                    print(f"{book['title']} is out of stock")
                elif book['stock'] < qty:
                    print(f"'{book['title']}' is under stock. {book['stock']} copies available")
                else:
                    book['stock'] -= qty
                    amount = qty * book['price']
                    print(f"{qty} copies of '{book['title']}' sold at {amount}")
                    print(f"{book['stock']} copies in stock")
                self.books[idx] = book
                return
        if not found:
            print(f"No matching book found")
            return
    
    def view_inventory(self):
        if not self.books:
            print("--- No Inventory Record ----")
            return
        print(f"{f"s/n":^3} {"Title":^20} {"Author":<15} {"Unit Price":^10}   {"Stock":^6}")
        print('-'*60)
        for idx, book in enumerate(self.books, 1):
            print(f"{f"{idx}.":<3} {book['title']:<20} {book['author']:<15} #{book['price']:>9.2f}   {book['stock']:>5}")

    def search_by_title(self, query):
        return [book for book in self.books if query.lower() in book["title"].lower()]
