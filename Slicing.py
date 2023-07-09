name = "kartik "
# slicing = create a substring by extracting elements from another string
#two colons means skipping ever n -1
# indexing [] or slice ()
#     [start:stop:step]

first_name = name[:3]
last_name = name[4:]
funky_name = name[::3]
rev = name[::-1]



webiste = "http://google.com"
slice = slice(7,-4)

print(webiste[slice])