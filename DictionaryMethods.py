#DICTIONARY METHODS

fruit = {
     "name": "Apple",
     "colour": "Red",
}

fruit.clear()
print(fruit)

fruit = {
     "name": "Apple",
     "colour": "Red",
}

fruit.copy()
print(fruit)

#fromkeys()=Returns a dictionary with the specified keys and value
x = ('note1','note2','note3')
y = '$'
thisdict = dict.fromkeys(x,y)
print(thisdict)

p = fruit.get("colour")
print(p)

q = fruit.items()
print(q)

fruit["cost"] = 20

r = fruit.keys()
print(r)

fruit.pop('cost')
print(fruit)

fruit.popitem()
print(fruit)

fruit["colour"] = "Red"
fruit["cost"] = 20

s = fruit.setdefault("colour")
print(s)

fruit.update({"colour1": "DarkRed"})
print(fruit)

t = fruit.values()
print(t)

#OUTPUT:
9666810672
{}
{'name': 'Apple', 'colour': 'Red'}
{'note1': '$', 'note2': '$', 'note3': '$'}
Red
dict_items([('name', 'Apple'), ('colour', 'Red')])
dict_keys(['name', 'colour', 'cost'])
{'name': 'Apple', 'colour': 'Red'}
{'name': 'Apple'}
Red
{'name': 'Apple', 'colour': 'Red', 'cost': 20, 'colour1': 'DarkRed'}
dict_values(['Apple', 'Red', 20, 'DarkRed'])
