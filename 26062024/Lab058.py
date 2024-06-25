#Filters

numbers= [1,2,3,4,5,6,7,8,9,10]

def is_even(num):
    return num%2 ==0

new_number=filter(is_even,numbers)
print(list(new_number))