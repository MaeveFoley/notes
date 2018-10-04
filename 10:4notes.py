#random: generates something random (a number, item from a list, etc.)
#syntax for random:
import random #(as *insert shorthand*, or from random import * *))

#example:

number = random.randint(5,7)
print(number)

myList = [1, "hello", 10, "Sacred Heart", "Long weekend"]
selectitem = random.choice(myList)
print(selectitem)
