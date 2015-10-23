#Problem 5
#---------------------------------------------------------------------------------------------------------------------------------
#Smallest multiple
#---------------------------------------------------------------------------------------------------------------------------------
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#---------------------------------------------------------------------------------------------------------------------------------

#First Solution

startNumber = 2520
fl = 1
while True:
    for x in xrange(1,21,1):
        if startNumber % x != 0:
            fl = 0
    if fl == 0:
        startNumber += 1
        print(str(startNumber))
        fl = 1
    else:
        print("smallest positive number: " + str(startNumber))
        break