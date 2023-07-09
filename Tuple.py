#tuple = collection which is ordered and unchangeable used to group together related data

student = ("Bro", 21,"male")

print(student.count("Bro"))
print(student.index("male"))

for i in student:
    print(i , end="")
    print(" ", end = "")
print()

if "Bro" in student:
    print("Bro is found")