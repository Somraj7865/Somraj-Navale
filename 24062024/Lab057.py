#Dictonary

my_dict={"name":"Somraj", "age":"30", "address":"Nashik"}
print(my_dict)
print(len(my_dict))

print(my_dict["age"])

phone_book=dict(name="Somraj",age="30")
print(phone_book)

print(phone_book.keys())
print(phone_book.values())

for k,v in phone_book.items():
    print(k,v)
