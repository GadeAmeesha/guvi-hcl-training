# Global variable
cart = []

def add_item(item):
    cart.append(item)   # using global list
    print(f"{item} added to cart.")

def view_cart():
    print("Your Cart:", cart)

add_item("Apples")
add_item("Milk")
view_cart()


balance = 1000   # Global variable

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited {amount}, Balance = {balance}")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrew {amount}, Balance = {balance}")
    else:
        print("Insufficient funds!")

deposit(500)
withdraw(300)
withdraw(1500)
