#                                              ╔══════════════════════╗        
#                                              ║---------DAY-2--------║
#                                              ╚══════════════════════╝
# --------------------------------------------------------------------------------------------------------------------------------------------
# # 1. Swapping of Two Numbers ?
# # Method:1 Using a third variable ?
# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# c=a
# a=b
# b=c
# print("After Swapping:")
# print("a =",a)
# print("b =",b)
# --------------------------------------------------------------------------------------------------------------------------------------------
# #Method:2 Without a third variable ? 
# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# a=a+b
# b=a-b
# a=a-b
# print("After Swapping:")
# print("a =",a)
# print("b =",b)
# --------------------------------------------------------------------------------------------------------------------------------------------
# #Method:3 Using multiplication/division ?
# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))

# a = a * b
# b = a // b
# a = a // b

# print("After Swapping:")
# print("a =", a)
# print("b =", b)
# --------------------------------------------------------------------------------------------------------------------------------------------
#2.Check whether a given triangle is a valid triangle or not ?
#Explaination:
# To check whether three given sides form a valid triangle, use the Triangle Inequality Theorem:
# The sum of any two sides must be greater than the third side.
# a + b > c
# a + c > b
# b + c > a

# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# c = int(input("Enter the value of c: "))

# if a + b > c and a + c > b and b + c > a:
#     print("The given sides form a valid triangle.")
# else:
#     print("The given sides do not form a valid triangle.")
# --------------------------------------------------------------------------------------------------------------------------------------------
#3. Check whether a triangle is Equilateral, Isosceles, or Scalene ? 
# Given three sides a, b, and c:

# Equilateral → all three sides are equal
# Isosceles → any two sides are equal
# Scalene → all three sides are different

# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# c = int(input("Enter the value of c: "))

# if a == b and b == c:
#     print("Equilateral Triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")
# --------------------------------------------------------------------------------------------------------------------------------------------
#4.Write the code to display the factorial of a number ? 
# Logic:
# fact = 1
# 1 × 1 = 1
# 1 × 2 = 2
# 2 × 3 = 6
# 6 × 4 = 24
# 24 × 5 = 120

# n = int(input("Enter a number: "))

# fact = 1

# for i in range(1, n+1):
#     fact = fact * i

# print("Factorial:", fact)
# --------------------------------------------------------------------------------------------------------------------------------------------
#5. Display the pairs whose sum is 100 ? 
# for a in range(1, 100):
#     b = 100 - a
#     print(a, "+", b, "=", 100)
# --------------------------------------------------------------------------------------------------------------------------------------------
 #6.Determine the prime number using functions ?
 
# def primeNum(n):
#     if n<2 :
#         return False
#     for i in range(2,n,1):
#         if n%i==0:
#             return False
#     return True
# print(primeNum(3))  