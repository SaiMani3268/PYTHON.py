#LIST METHODS
#Used lists are l1,l2,l3,fruits

l1 = [1,6,3,9,5,6,7,8,9]
l2 = ['a','b','c','d','e']
#append()=add an element at the end
l1.append(10)
print(l1)

#clear()=removes all elemnets
l1.clear()
print(l1)

#copy()=displays elements in the list
x=l1.copy()
print(x)
y=l2.copy()
print(y)

#count()=displays number of times a specified value is present
l1 = [1,6,3,9,5,6,7,8,9]
x=l1.count(6)
print(x)
y=l2.count('a')
print(y)

#extend()=combines 2 lists
l1.extend(l2)
print(l1)

#index()=prints index of specified value
x=l1.index(9)
print(x)

#insert()=adds/inserts specified value at specified position
l1.insert(3,4)
print(l1)

#pop()=deletes element at specified position 
l1.pop(4)
print(l1)

#remove()=removes specified value in the list 
l1.remove(6)
print(l1)

#reverse()=reverse the elements in the list
l1.reverse()
print(l1)

#sort()=sorts elements in the list
l3 = [1,5,6,7,4,3,7]
l3.sort(reverse=True)
print(l3)
l3.sort()
print(l3)

def myFun(e):
  return len(e)
fruits = ['apple','orange','kiwi','banana']
fruits.sort(key=myFun)
print(fruits)


#OUTPUT:-
#[1, 6, 3, 9, 5, 6, 7, 8, 9, 10]
#[]
#[]
#['a', 'b', 'c', 'd', 'e']
#2
#1
#[1, 6, 3, 9, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
#[1, 6, 3, 4, 9, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
#[1, 6, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
#[1, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
#['e', 'd', 'c', 'b', 'a', 9, 8, 7, 6, 5, 4, 3, 1]
#[7, 7, 6, 5, 4, 3, 1]
#[1, 3, 4, 5, 6, 7, 7]
#['kiwi', 'apple', 'orange', 'banana']
