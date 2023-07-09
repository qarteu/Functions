#set = collection which is unordered, unindexed. No dup values

utensils = {"fork", "spoon", "knife","knife","knife"}
dishes = {"bowl", "cup", "straw", "knife"}
utensils.add("napkin")
#utensils.update(dishes)
table = utensils.union(dishes)

for x in  table:
    print(x + " ", end ="")

print()
print()


#what does utensils have that dishes dont
print(utensils.difference(dishes))
#what does dishes have that utensils dont
print(dishes.difference(utensils))
print(utensils.intersection(dishes))






