rows = int(input("How many rows:"))
cols = int(input("How many columns:"))
sym = input("Enter symbol to use:")

for i in range(rows):
    for j in range(cols):
        print(sym, end = "")
    print()