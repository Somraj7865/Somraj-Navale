#Multilevel inheritance
class grandfather():
    keygold="2kg"
    def grandpa(self):
        print("grandfather method")

class father(grandfather):
    key="1kg"
    def father(self):
        print("father method")

class son(father):
    def son(self):
        print("son method")

son1=son()
print(son1.keygold)
son1.grandpa()
son1.father()
son1.son()