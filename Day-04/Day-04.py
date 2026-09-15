#                                             ╔══════════════════════╗        
#                                             ║---------DAY-4--------║
#                                             ╚══════════════════════╝

# ---------------------------------------------------------------------------------------------------------------------------------
# 1.“Write a Python program to check whether a given number is a palindrome or not.” ?  ⭐⭐⭐⭐⭐
# Input: 121
# Output: 121 is a Palindrome

# n=int(input("Enter a Number:"))
# original = n
# reverse = 0
# while n>0:
#     digit =n%10
#     reverse = reverse * 10 + digit
#     n = n//10
# if original==reverse:
#     print(original,"It is a Palindrome Number")
# else :
#     print(original,"It is Not a Palindrome")
# ---------------------------------------------------------------------------------------------------------------------------------
# 2. Write a Python program to print all palindrome numbers from 0 to 1000 ?  ⭐⭐⭐⭐⭐
# for  i in range (1,1001,1):
#     original = i
#     reverse = 0
#     while i>0:
#         digit = i%10
#         reverse = reverse * 10 + digit
#         i= i//10
#     if original == reverse:
#         print(original)
# ---------------------------------------------------------------------------------------------------------------------------------
#3.“Write a Python program using a function to check whether a given number is a palindrome or not.” ?  [WITH INPUT & WITHOUT RETURN]
# def checkPalindrome(n):
#     original = n
#     reverse = 0

#     while n > 0:
#         digit = n % 10
#         reverse = reverse * 10 + digit
#         n = n // 10

#     if original == reverse:
#         print(original, "is Palindrome")
#     else:
#         print(original, "is Not Palindrome")


# n = int(input("Enter a number: "))
# checkPalindrome(n)
# ---------------------------------------------------------------------------------------------------------------------------------
# 4.  “Write a Python program to check whether a given number is an Armstrong number or not ? 
# n = int(input("Enter a number: "))

# original = n
# power = len(str(n))
# sum = 0

# while n > 0:
#     digit = n % 10
#     sum = sum + digit ** power
#     n = n // 10

# if original == sum:
#     print(original, "is Armstrong")
# else:
#     print(original, "is Not Armstrong")
# ---------------------------------------------------------------------------------------------------------------------------------
# 5.“Write a Python program to find all Armstrong numbers within a given range ? 

# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))

# for num in range(start, end + 1):

#     original = num
#     n = num
#     digits = len(str(num))
#     total = 0

#     while n > 0:
#         digit = n % 10
#         total = total + digit ** digits
#         n = n // 10

#     if original == total:
#         print(original, end=" ")
# ---------------------------------------------------------------------------------------------------------------------------------
# 6.“Write a Python program to generate the Fibonacci series up to N terms.”
# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
    
#     c = a + b
#     a = b
#     b = c
# ---------------------------------------------------------------------------------------------------------------------------------
# 7.Write a Python program to print the Fibonacci series up to a given limit ?
limit = int(input("Enter the limit: "))

a = 0
b = 1

while a <= limit:
    print(a, end=" ")

    c = a + b
    a = b
    b = c