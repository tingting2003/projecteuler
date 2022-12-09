'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

n = a * b * ... * z * ??
a, b, .. z <= sqrt(n)
?? no factors <= sqrt(n)
?? = 1 or ?? > sqrt(n)
'''
MAXN = 1000000
# isPrime = [True for i in range(MAXN)]
isPrime = []
for i in range(MAXN):
    isPrime.append(True)
isPrime[1] = False

for i in range(2, MAXN):
    if isPrime[i]:
        for j in range(i * 2, MAXN, i):
            isPrime[j] = False
# print(isPrime)

prime = []
for i in range(len(isPrime)):
    if isPrime[i]:
        prime.append(i)
# print(prime)

largestPrimeFactor = 0
# n = 600851475143
n = 1000003000000
for i in range(1, len(prime)):
    if n % prime[i] == 0:
        largestPrimeFactor = prime[i]
        while n % prime[i] == 0:
            n = n // prime[i]
    else:
        continue

if n > 1:
    largestPrimeFactor = n
print(largestPrimeFactor)