#                                              ╔══════════════════════╗        
#                                              ║---------DAY-3--------║
#                                              ╚══════════════════════╝
# ----------------------------------------------------------------------------------------------------------------------------------------------

# 1. Write a Python program to check whether the given year is a leap year or not ?

# Rules:
# The year is divisible by 400, OR
# The year is divisible by 4 but not divisible by 100 ?

# Main Topic:Conditional Statements
# Sub-Topics:if-else, logical operators, % modulus, divisibility

# year=int(input("Enter a year :"))

# if (year%400==0 or year%4==0) and  year%100!=0:

#     print(year, "= is leap year") 

# else:

#     print("Not a leap year")

# ----------------------------------------------------------------------------------------------------------------------------------------------
# 2.Write a Python program to check whether a number is even or odd only if it is positive. If the number is negative, display that it is a negative number ?

# Main Topic: Nested if Statement
# Sub-Topics: if-else, nested if, % modulus, comparison operators

# n = int(input("Enter a number: "))

# if n > 0:
#     print(n, "is a positive number")

#     if n % 2 == 0:
#         print(n, "is an even number")
#     else:
#         print(n, "is an odd number")
# else:
#     print(n, "is a negative number")
# ----------------------------------------------------------------------------------------------------------------------------------------------
# 3.Write a Python program using match-case to display a restaurant menu with 5 food items. Ask the user to select an option and display the selected item's name, price, 
# and description. For an invalid choice, display Invalid choice ??

# Main Topic:match-case Statement 
# Sub-Topics:match, case, case _, user input, menu selection

# print("===============================Menu===============================")
# print("1.Biryani")
# print("2.Fish Fry")
# print("3.Mutton Biryani")
# print("4.Grill Chicken")
# print("5.Tandoori Chicken")
# option=int(input("Enter Your Favorite Food:"))

# match option:
#     case 1:
#         print("Item: Biriyani")
#         print("Price: 250")
#     case 2:
#             print("Item: Fish Fry")
#             print("Price: 180")
#     case 3:
#             print("Item: Mutton Biryani")
#             print("Price: 300")
#     case 4:
#             print("Item: Grill Chicken")
#             print("Price: 150")
#     case 5:
#             print("Item: Tandoori Chicken")
#             print("Price: 280")
#     case _:
#             print("Sorry Item not Available 😔")
# ----------------------------------------------------------------------------------------------------------------------------------------------
# Topic: String Concatenation with User Input

# 4.Write a Python program to accept the user's first name and last name, concatenate them, and display the complete name.

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# full_name = first_name + " " + last_name

# print("Full Name:", full_name)
# ----------------------------------------------------------------------------------------------------------------------------------------------
# 5.Write a Python program to check whether a given number is a prime number or not using a for loop ?
# Topic:Loops

# n = int(input("Enter a number: "))

# count = 0

# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1

# if count == 2:
#     print(n, "is a prime number")
# else:
#     print(n, "is not a prime number")
# ----------------------------------------------------------------------------------------------------------------------------------------------
#6.Skip the odd given Number in the given Number n=63841
# n=63841
# while n!=0:
#     ld= n%10
#     if ld%2!=0:
#         n=n//10
#         continue
#     print("ODD Number = ", ld)
#     n=n//10   