
food = ["pizza", "rice", "cake", "hotdog"]
food[0] = "sushi"
food.append("icecream") #add to last
food.remove("hotdog")
food.pop() #remove last
food.clear()

for f in food:
    print(f + " " , end="")

print(food)