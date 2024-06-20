def outer_fun():
    var1 = 100

    def inner_fun():
        print(var1)

    inner_fun()


outer_fun()
