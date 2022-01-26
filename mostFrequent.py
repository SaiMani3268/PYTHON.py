#most_frequent function which takes a string and prints letters in descending order of frequency

import operator
def most_frequent(string):
   print("The original string is:",string)
   d = dict()
   for key in string:
       if key not in d:
           d[key] = 1
       else:
           d[key] = d[key] + 1
   print("String in dictionary with frequency values is:\n",d)
   sort_d = sorted(d.items(),key = operator.itemgetter(1),reverse = True)
   print("Sorted descending order w.r.t frequency is:\n",sort_d)
most_frequent('mississippi')

#OUTPUT:
#The original string is: mississippi
#String in dictionary with frequency values is:
# {'m': 1, 'i': 4, 's': 4, 'p': 2}
#Sorted descending order w.r.t frequency is:
# [('i', 4), ('s', 4), ('p', 2), ('m', 1)]