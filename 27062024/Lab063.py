class dog():
    name = None

    def sleep(self):
        print("Sleeping")


dog1 = dog()
dog2=dog()
print(dog1.name)
dog1.name = "Chaw"
print(dog1.name)
dog1.sleep()
print("************************************")
print(dog2.name)
dog2.name = "Maw"
print(dog2.name)

dog2.sleep()