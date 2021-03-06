#Problem 1
#---------------------------------------------------------------------------------------------------------------------------------
#Multiples of 3 and 5
#---------------------------------------------------------------------------------------------------------------------------------
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
#---------------------------------------------------------------------------------------------------------------------------------

#First Solution
summ = 0
for x in xrange(1000):
    if x % 3 == 0 or x % 5 == 0:
        summ = summ + x
print("sum: " + str(summ))

#Optimal Solution
