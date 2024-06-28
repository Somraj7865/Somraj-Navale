class BankAccount:

    def __init__(self):
        self.balance = 0
        self.__privatevar = 100

    def public_fun(self):
        print(self.__privatevar)

    def deposite(self, amount):
        self.balance += amount

    def __withdraw(self, amount):
        self.balance -= amount

    def __showbalance(self):
        print("Your balance is", self.balance)

    def if_you_are_auth(self, flag):
        if flag:
            print("You are allowed")
            self.__showbalance()
        else:
            print("Not allowed")

    def if_you_are_auth_user(self, flag, amount):
        if flag:
            self.__withdraw(amount=amount)
            self.__showbalance()
        else:
            print("Not allowed")


a = BankAccount()
a.deposite(100)
a.if_you_are_auth(True)
a.if_you_are_auth_user(True, 50)
