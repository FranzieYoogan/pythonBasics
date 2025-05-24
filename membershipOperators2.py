students = {"SpongeBob", "Patrick", "Sandy"}

student = input("Enter a student")

if student in students:
    print(f"{student} is a student")

else:
    print(f"{student} was not found")