import os

path = "C:\\Users\\Kartik\\....."

if os.path.exists(path):
    print("Exists!")
    if(os.path.isfile(path)):
        print("That is file")
    elif os.path.isdir(path):
        print("Directory")
else:
    print("That location doesnt exist")

