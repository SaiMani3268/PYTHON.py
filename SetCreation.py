#CREATE A SET

set1 = {"apple","banana","carrot","apple","door"}
set2 = set(("apple","banana","carrot","apple","door"))
set3 = {1,2,1,3,1,4,1,5,1,6}
set4 = {true,false,true}

print(set1)
print(len(set1))
print(set2)
print(len(set2))
print(set3)
print(len(set3))
print(set4)
print(len(set4))

#OUTPUT:
{'carrot', 'door', 'banana', 'apple'}
4
{'carrot', 'door', 'banana', 'apple'}
4
{1, 2, 3, 4, 5, 6}
6
{False, True}
2