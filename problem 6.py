'''The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

n = 100
# sum of the square
sumOfSqaure = 0
for i in range(n + 1):
    sumOfSqaure += i ** 2

# square of the sum
sumOfn = 0
for i in range(n + 1):
    sumOfn += i

squareOfSum = sumOfn ** 2
print(squareOfSum - sumOfSqaure)