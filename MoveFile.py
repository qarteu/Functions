import os

source = "test.txt"
destination = "copy past destination with double slashes"
try:
    if os.path.exists(destination):
        print("Duplicate found")
    else:
        os.replace(source,destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")