
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
    print(f"\n{'Bookstory Inventory System':^30}")

    inventory = Inventory()

    while True:
        print("\n--- Bookstore Menu ---")
        print("1. Add stock to Inventory")
        print("2. Sell book")
        print("3. View Inventory")
        print("4. Save and Exit")

        try:  
            choice = input("\nEnter your Choice: ")
        except:
            print("Invalid option: Choose from 1-4")
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
                print("Stock added to inventory")
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
                inventory.save_to_file()
                print('Saved...\nExiting... \nGoodbye!...')
                break
            case _:
                print("Invalid option: Choose from 1-4")
                continue

if __name__ == '__main__':
    main()