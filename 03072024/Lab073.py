class parent:
    gold = "2kg"
    def BHK2(self):

        print("2BHK")


class son(parent):
    def BHK3(self):
        print("3BHK")


son_object = son()
son_object.BHK3()
son_object.BHK2()
print(son_object.gold)
