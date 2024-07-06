#Exception, except and finally

try:

  num1=int(input("Enter first number: "))
  num2=int(input("Enter second number: "))
  res=num1/num2

except ValueError as val:
  print(val)

except ZeroDivisionError as zde:
    print(zde)
else:
    print(f'result is: {res}')

finally:
    print("This code will be executed anyhow!!")



