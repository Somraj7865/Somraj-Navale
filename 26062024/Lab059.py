#   map-->take one item and applay the function
#give the same number of elements
numbers=[1,2,3,4,5,6,7,8,9,10]

def nu(num):
    return num*2

double_numb=map(nu,numbers)
print(list(double_numb))

#filters-->take items check and return true items else reject

def even_giver(num):
    return num % 2 ==0

even_num=filter(even_giver,numbers)
print(list(even_num))