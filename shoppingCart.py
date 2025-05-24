item = input("Enter the item you want to add to your shopping cart: ")
price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

total = price * quantity
print(f"Item: {item}, quantity: {quantity}, total: {total}")