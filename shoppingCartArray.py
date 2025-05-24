foods = []
prices = []
total = 0

while True:
    food = input("Enter food(q to quit): ")
    if food.lower() == "q":
         break
    else:
     price = float(input("Enter the price ${food}: "))
     foods.append(food)
     prices.append(price)

print("------------FOOD CART ------------ \n")

for food in foods:
   print(food)

for price in prices:
   total += price

print(f"Total: {total}")