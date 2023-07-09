#dict = a changeable, unordered collection of unique key:value pairs
#       Fast because they use hashing, allow us to access a value quickly

cap = {'USA' : 'Washington DC',
       'India' : 'New Dehli',
       'Russia' : 'Moscow'}

cap.update({"Germany" : "Berlin"})
cap.update({'USA' : "LA"})
cap.pop('India')


print(cap['Russia'])
print(cap.get('Russia'))
print(cap.keys())
print(cap.values())
print(cap.items())
print(cap)


for key,value in cap.items():
    print(key,value)