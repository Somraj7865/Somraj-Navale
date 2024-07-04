#how to use super --> used to override a method
class A:
    def fun1(self):
        print("Somraj")

class B(A):

    def fun1(self):
        super().fun1()
        print("Navale")

b=B()
b.fun1()