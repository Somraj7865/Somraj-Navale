# Program to find a leap year or not
import math

year = int(input("Enter a year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year")
else:
    print("It is not a leap year")

#
# num = int(input("Enter a number:"))
# res=math.factorial(num)
# print(res)

