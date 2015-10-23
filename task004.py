#Problem 4
#---------------------------------------------------------------------------------------------------------------------------------
#Largest palindrome product
#---------------------------------------------------------------------------------------------------------------------------------

#Find the largest palindrome made from the product of two 3-digit numbers.
#---------------------------------------------------------------------------------------------------------------------------------

#First Solution

startNumber = 100
endNumber = 999
polindromList = [1]

while startNumber <= endNumber:
    tempNumber = 100
    while tempNumber <= endNumber:
        tempPolindrome = startNumber * tempNumber
        tempNumber += 1
        if str(tempPolindrome) == str(tempPolindrome)[::-1]:
            polindromList.append(tempPolindrome)
    startNumber += 1

print(max(polindromList))
