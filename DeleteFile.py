import os

path = "test.txt"

try:
    os.remove(path)
    #os.rmdir(path) remove directory
    #os.rmtree(path) delete full directory containing files

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Dont have permission")
else:
    print(path + "was deleted")