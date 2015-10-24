#Problem 6
#---------------------------------------------------------------------------------------------------------------------------------
#Sum square difference
#---------------------------------------------------------------------------------------------------------------------------------
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#---------------------------------------------------------------------------------------------------------------------------------

#First Solution

def squaresSum():

    ''' Find sum of the squares '''

    squaresList = [x*x for x in range(101)]
    sqSum = sum(squaresList)
    print("sum of squares: " + str(sqSum))
    
    return sqSum

def sumSquare():

    ''' Find square of the sum '''

    sumSq = pow(sum([x for x in range(101)]), 2)
    print("square of sum: " + str(sumSq))

    return sumSq

def difference():

    ''' The answer generation '''

    a = squaresSum()
    b = sumSquare()

    return b-a

print("difference: " + str(difference()))

