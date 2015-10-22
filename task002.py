#Problem 1
#---------------------------------------------------------------------------------------------------------------------------------
#Even Fibonacci numbers
#---------------------------------------------------------------------------------------------------------------------------------
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#---------------------------------------------------------------------------------------------------------------------------------

#First Solution

summ = 0
a,b = 1,1
listFib = [1]

while True:
    if (a + b) < 4000000:
        listFib.append(a + b)
        if (a + b) % 2 == 0:
            summ = summ + a + b
        a = b
        b = listFib[-1]
    else: 
        break

print("sum: " + str(summ))

#Optimal Solution
#Every tird number in Fibonacci sequence is even 2, 8, 34, 144,..

summ = 0
a,b = 1,1
c = a + b

while c < 4000000:
    summ = summ + c
    #1 2 3 5 8 13
    #1 2 3
    a = b + c #5
    b = a + c #8
    c = a + b #13 

print("optimal sum: " + str(summ))
