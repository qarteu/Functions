
#break --> terminate the loop entirely
#continue --> skips to the next iteration of the loop
# pass --> does nothing, acts as a placeholder

while True:
    name = input("Enter you name: ")
    if name != "":
        break
ph = "123-456-0494"
for i in ph:
    if i =="-":
        continue
    print(i,end="")

print()

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i,end="")

