
import os
import json

FILE_PATH = 'Bookstore_Inventory_System/inventory.json'

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

def load_invetory():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        inventories = json.load(file)
        return inventories
    
def save_inventory(inventories):
    with open(FILE_PATH, 'w') as fp:
        json.dump(inventories, fp, indent=2)

class Inventory:
    def __init__(self):
        self.inventories = load_invetory()
    
    def add_to_inventory(self, book: Book):
        book_dict = book.to_dict()
        self.inventories.append(book_dict)
    
    def sell_book(self, title, qty):
        found = False
        for idx, book in enumerate(self.inventories, 0):
            if book['title'].lower() == title.lower():
                found = True
                if book['stock'] == 0:
                    print(f"{book['title']} is out of stock")
                elif book['stock'] < qty:
                    print(f"{book['title']} is under stock. {book['stock']} copies available")
                else:
                    book['stock'] -= qty
                    amount = qty * book['price']
                    print(f"{qty} copies of '{book['title']}' sold at {amount}")
                    print(f"{book['stock']} copies in stock")
                self.inventories[idx] = book
                return
        if not found:
            print(f"Book not found")
            return
    
    def view_inventory(self):
        if not self.inventories:
            print("--- No Inventory Record ----")
            return
        print('-'*50)
        for idx, book in enumerate(self.inventories, 1):
            print(f"{idx}. {book['title']} - {book['author']} - {book['price']} - {book['stock']}")

    def save_to_file(self):
        save_inventory(self.inventories)
