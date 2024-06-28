class student:

    def __init__(self):
        self.name=input("Enter a name: ")
        self.age=input("Enter an age: ")

    def display(self):
        print(f"{self.name} age is {self.age}")

stu=student()
stu.display()