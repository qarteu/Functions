#args = parameter that will pack all arguments into a tuple useful so that a function can accept a varying amount of arugments

def add(*args):
   sum = 0
   args = list(args)
   args[0] = 0
   for i in args:
       sum += i
   return sum



print(add(1,2,3))