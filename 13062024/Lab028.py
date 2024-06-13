# Write a program to print the grades
score = int(input("Enter the score: "))
if score > 90 and score < 100:
    print("A")
elif score > 80 and score < 90:
    print("B")
elif score > 70 and score < 80:
    print("C")
elif score > 60 and score < 70:
    print("D")
else:
    print("Invald score")
