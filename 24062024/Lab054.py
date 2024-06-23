#Set
list_of_uniq_items={1,2,3,3,4,5,5}
print(list_of_uniq_items)


list=[1,1,2,3,3,4]
set1=set(list)
print(set1)
print(len(set1))

set1={1,2,3,4}
set2={3,4,5,6}
print(set1.intersection(set2))

print(set2.difference(set1))

set2.remove(6)
print(set2)

set2.add(7)
print(set2)