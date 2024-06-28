#Encapsulation
class myclass:

    def __init__(self):
        self.name="Somraj"


    def __private_fun(self):
        print("This is private function")

    def public_fun(self):
        print("This is public")

    def public_private_fun(self):
        self.__private_fun()
a=myclass()
a.public_fun()
a.public_private_fun()