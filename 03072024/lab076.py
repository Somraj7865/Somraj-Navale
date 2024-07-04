# Multiple inheritance
class A:
    def method(self):
        return "Method A"


class B:
    def method(self):
        return "Method B"


class C(A, B):
    pass


#        return "Method C"


c = C()
print(c.method())
