# Inheritance

class grandfather:
    key = "abc@123"

    def grandfather_method(self):
        return "grandfathers method"


class farher(grandfather):
    def father_method(self):
        return "farhers method"


parentt = farher()
print(parentt.father_method())
print(parentt.grandfather_method())
print(parentt.key)
