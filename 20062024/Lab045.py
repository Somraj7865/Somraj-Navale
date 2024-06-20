numbers= [1,2,3]

def mylist(numbers):
    numbers.append(4)
    numbers[0]=100
    return numbers


new_list=mylist(numbers)
print(new_list)
