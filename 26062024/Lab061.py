#Leet code - sum of digits
number=12345

r1=number%10
print(r1)
q1=number//10
print(q1)

r2=q1%10
print(r2)
q2=q1//10
print(q2)

r3=q2%10
print(r3)
q3=q2//10
print(q3)

r4=q3%10
print(r4)
q4=q3//10
print(q4)

r5=q4%10
print(r5)
q5=q4//10
print(q5)


print(r1+r2+r3+r4+r5)

#now above prog by using recursion

def add(n):
    if n<10:
        return 1
    else:
        return n%10 + add(n//10)


print(add(12345))