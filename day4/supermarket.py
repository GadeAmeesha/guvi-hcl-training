import datetime

total = 0
bill_items = []   # to store purchased items

# Chocolate Section
def cho():
    global total
    print("1. 20 Rs Chocolate")
    print("2. 10 Rs Chocolate")
    fop = int(input("Select Chocolate Option: "))
    q = int(input("Enter Quantity: "))

    if fop == 1:
        stot = 20 * q
        item = f"20 Rs Chocolate x {q}"
    elif fop == 2:
        stot = 10 * q
        item = f"10 Rs Chocolate x {q}"
    else:
        print("Invalid option")
        return
    
    total += stot
    bill_items.append((item, stot))
    print(f"Added: {item} = {stot}")
    print("Grand total till now = ", total)


# Biscuit Section
def bis():
    global total
    print("1. 15 Rs Biscuit")
    print("2. 5 Rs Biscuit")
    fop = int(input("Select Biscuit Option: "))
    q = int(input("Enter Quantity: "))

    if fop == 1:
        stot = 15 * q
        item = f"15 Rs Biscuit x {q}"
    elif fop == 2:
        stot = 5 * q
        item = f"5 Rs Biscuit x {q}"
    else:
        print("Invalid option")
        return
    
    total += stot
    bill_items.append((item, stot))
    print(f"Added: {item} = {stot}")
    print("Grand total till now = ", total)


# Main Program
name = input("Enter Customer Name: ")
phone = input("Enter Phone Number: ")
now = datetime.datetime.now()

while True:
    print("\n--- Welcome to XYZ Gro ---")
    print("1. Chocolate\n2. Biscuit\n3. EXIT & PRINT BILL")
    op = int(input("Select your option: "))

    if op == 1:
        cho()
    elif op == 2:
        bis()
    elif op == 3:
        break
    else:
        print("Invalid choice, try again!")


bill_text = "\n===== XYZ GRO BILL =====\n"
bill_text += f"Date: {now.strftime('%d-%m-%Y %H:%M:%S')}\n"
bill_text += f"Customer: {name}\nPhone: {phone}\n"
bill_text += "-----------------------------\n"
bill_text += "Items Purchased:\n"

for item, price in bill_items:
    bill_text += f"{item} = Rs.{price}\n"

bill_text += "-----------------------------\n"
bill_text += f"Grand Total = Rs.{total}\n"
bill_text += "===== THANK YOU! VISIT AGAIN =====\n"

print(bill_text)


with open("supermarket_bill.txt", "a") as f:
    f.write(bill_text + "\n\n")
