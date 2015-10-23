#Problem 3
#---------------------------------------------------------------------------------------------------------------------------------
#Largest prime factor
#---------------------------------------------------------------------------------------------------------------------------------
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#---------------------------------------------------------------------------------------------------------------------------------

#First Solution

largestPrimeFactorList = [1]
currentPrimeFactor = 2
currentTargetNumber = 600851475143

while currentTargetNumber > 1:
    if currentTargetNumber % currentPrimeFactor == 0:
        largestPrimeFactorList.append(currentPrimeFactor)
        currentTargetNumber = currentTargetNumber / currentPrimeFactor
    else: 
        currentPrimeFactor += 1

print(max(largestPrimeFactorList))
