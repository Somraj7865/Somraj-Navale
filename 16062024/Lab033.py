# # num = int(input("Enter a number"))
# match num:
#   case 1:
# #      print("You entered 1")
# # case 2:
# # print("You entered 2")
# # case _:
# # print("You entered other than number")

num = int(input("Enter a number: "))
match num:
    case 1:
        print("You entered 1")
    case 2:
        print("You entered 2")
    case _:
        print("You entered something other than 1 or 2")