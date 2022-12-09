'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
n = 1000
palindrome =[]

for i in range(100, n):
    for j in range(100, n):
        product = i * j
        product = str(product)
        for k in range(len(product) // 2):  # for k in 4
            if product[k] == product[-(k + 1)]:
                if k == len(product) // 2 - 1:
                    palindrome.append(product)
            else:
                break
print(palindrome)

largerPalindrome = 0

for i in range(len(palindrome)):
    if int(palindrome[i]) > largerPalindrome:
        largerPalindrome = int(palindrome[i])
print(largerPalindrome)
