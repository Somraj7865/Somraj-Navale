class car:

    def __init__(self,name, version, model):
        self.name=name
        self.version=version
        self.model=model

    def engine(self):
        print("Starting a car with name", self.name)
        print("Starting a car with version", self.version)
        print("Starting a car with model", self.model)


lambo=car("Lamborgni", "V01", "2024")
lambo.engine()
print("**************************")
farar=car("Farari", "V02", "2024")
farar.engine()



