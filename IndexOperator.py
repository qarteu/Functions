#index operator [] = gives access to a sequnces element (str,list,tuples)

name = "kartik Malunjkar"

if name[0] == "a":
    print("YEP")

if name[0].islower():
    name = name.capitalize()

first_name =  name[0:6].upper()
last_char = name[-1]

print(first_name)
print(last_char)

print(name)