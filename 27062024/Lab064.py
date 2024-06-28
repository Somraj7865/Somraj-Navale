class dog():
    name = None
    id = None

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def sleep(self):
            print(" Who is sleeping-->", self.name)


dog1 = dog("chaw", "1")
dog2 = dog("maw", "2")

print(f'{dog1.name} has id {dog1.id}')
print(f'{dog2.name} has id {dog2.id}')

dog1.sleep()
dog2.sleep()
