'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.'''

n = 1000
total = 0
for i in range(0, n, 3):
    total += i
for i in range(0, n, 5):
    if i % 3 == 0:
        continue
    else:
        total += i

print(total)

# alternative

for i in range(0, n):
    if i % 3 == 0 or i % 5 == 0:
        total += i

# alternative2

total = 0
n -= 1
num3 = n // 3
# 1 + 2 + ... + x = x * (x + 1) // 2
total += 3 * (num3 * (num3 + 1) // 2)
num5 = n // 5
total += 5 * (num5 * (num5 + 1) // 2)
num15 = n // 15
total -= 15 * (num15 * (num15 + 1) // 2)
print(total)
