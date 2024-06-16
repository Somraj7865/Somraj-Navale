def python_class(name):
    match name:
        case "dell":
            print("dell is allowed")
        case "ram":
            print("ram is allowed")
        case _:
            print("Not allowed")
python_class("ghhj")
#
# def python_class(name):
#     match name:
#         case "dell":
#             print("dell is allowed")
#         case "ram":
#             print("ram is allowed")
#         case _:
#             print("Not allowed")
#
# # Call the function
# python_class("ram")