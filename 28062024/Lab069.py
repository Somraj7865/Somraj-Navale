class login:
    email=None
    password=None

    def __init__(self, email, password):
        self.email=email
        self.password=password

    def cred(self):
        if self.password == "123456":
            print("Allowed to enter")
        else:
            print("Not allowed")

var=login("somrajnavale@gmail.com", "1234")
var.cred()