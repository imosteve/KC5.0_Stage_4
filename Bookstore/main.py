
from inventory import Book, Inventory

def get_input(prompt):
    try:
        if prompt == 'stock':
            my_input = int(input(f"Enter book {prompt}: "))
        elif prompt == 'price':
            my_input = float(input(f"Enter book {prompt}: "))
            my_input = round(my_input, 2)
        else:
            my_input = input(F"Enter book {prompt}: ").title()
            my_input = " ".join(my_input.split())
        if my_input == "":
            print(f"{prompt} cannot be blank")
            return None
        return my_input
    except:
        print("Invalid input")
        return None

def main():
    print(f"\n{'Bookstore Inventory System':^30}")

    inventory = Inventory()

    while True:
        print("\n--- Bookstore Menu ---")
        print("1. Add stock to Inventory")
        print("2. Sell book")
        print("3. View Inventory")
        print("4. Search Book by Title")
        print("5. Exit")

        try:  
            choice = input("\nEnter your Choice: ")
        except:
            print("Invalid option: Choose from 1-5")
            continue
        
        match choice:
            case '1':
                title = get_input('title')
                if not title:
                    continue
                author = get_input('author')
                if not author:
                    continue
                price = get_input('price')
                if not price:
                    continue
                stock = get_input('stock')
                if not stock:
                    continue
                book = Book(title, author, price, stock)
                inventory.add_to_inventory(book)
                print("Book added to inventory")
            case '2':
                title = get_input('title')
                if not title:
                    continue
                qty = get_input('stock')
                if not qty:
                    continue
                inventory.sell_book(title, qty)
            case '3':
                inventory.view_inventory()
            case '4':
                query = input("Enter title to search: ")
                query = " ".join(query.split())
                results = inventory.search_by_title(query)
                if results:
                    for book in results:
                        print(f"{book['title']} by {book['author']} - ${book['price']}")
                else:
                    print("No matching books found.")
            case '5':
                inventory.save_books()
                print('Goodbye!...\n')
                break
            case _:
                print("Invalid option: Choose from 1-5")
                continue

if __name__ == '__main__':
    main()