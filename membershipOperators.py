word = "APPLE"

letter = input("Enter a Letter: ")

if letter.upper() in word:
    print(f"There is a {letter}")

else:
    print(f"There isn't a {letter}")