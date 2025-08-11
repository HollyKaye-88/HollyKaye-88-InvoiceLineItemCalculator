#Holly Gell
#CIS261
#Invoice Line Item Calculator


def get_price ():
    while True:
        try:
            value = input("Enter price: ")
            price = float(value)
            return price
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            pass

def get_quantity():
    while True:
        try:
            value = input("Enter quantity: ")
            quantity = int(value)
            return quantity
        except ValueError:
            print("Please enter a valid integer.")
            pass    


def main (): 
            print("The Invoice Line Item Calculator\n")
            more = 'y'
            while more.lower() == 'y':
                price = get_price()
                quantity = get_quantity()
                total = price * quantity
            
                print(f"Price: {price:.2f}")
                print(f"Quantity: {quantity}")
                print(f"Total: {total:.2f}\n")
                more = input("Enter another line item? (y/n): ")

            print("Bye!")

if __name__ == "__main__":
            main()     