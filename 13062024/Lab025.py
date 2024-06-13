# Program to find maximum among three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print("number1 is greater than number2 and number3")
elif num2 > num3 and num2 > num1:
        print("number2 is greater than number1 and number3")
else:
        print("number3 is greater than number 1 and number2")