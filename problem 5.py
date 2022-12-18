'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
# number is too big for this method
n = 20
for i in range(10000000, 1000000000):
    wantToBreak = False
    for j in range(1, n + 1):
        if i % j == 0:
            if j == n:
                print(i)
                wantToBreak = True
        else:
            break
    if wantToBreak:
        break

# a > b
# newa = b, newb = a % b
# O(log_2(max(a, b)))
# gcd(a, b) = gcd(b, a % b)
# gcd(a, 0) = a
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

import math
ans = 2
for i in range(3, n + 1):
    ans = ans * i // gcd(ans, i)
print(ans)