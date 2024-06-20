#Lambda expression
#used to do the task in one line

def double_mysalary(salary):
    salary=salary*2
    return salary
s= double_mysalary(100)
print(s)

#To print above all in one line use lambda expression like below

f_d_msalary=lambda salary:salary*2
print(f_d_msalary(100))