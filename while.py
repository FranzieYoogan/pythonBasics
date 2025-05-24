name = input("Enter your name: ")

while name == "":
    print("Name cannot be empty")
    name = input("Enter your name: ")

print(f"Hello {name}")