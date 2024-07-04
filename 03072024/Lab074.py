# Hirarchical inheritance
class father:
    def BHK1(self):
        print("1BHK")


class somraj(father):
    def BHK2(self):
        print("2BHK")


class vikas(father):
    def BHK3(self):
            print("3BHK")


som = somraj()
som.BHK2()
som.BHK1()

vik = vikas()
vik.BHK3()
vik.BHK1()
