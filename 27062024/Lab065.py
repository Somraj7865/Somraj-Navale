#Calculator
class calc:

    def add(self,a,b):
        return a+b

    def sub(self, a, b):
        return a - b


    def mul(self, a, b):
     return a * b


    def div(self, a, b):
     return a / b

cal_ref=calc()
output1=cal_ref.add(3,4)
print(output1)
output2=cal_ref.sub(3,4)
print(output2)
output3=cal_ref.mul(3,4)
print(output3)
output4=cal_ref.div(10,5)
print(output4)