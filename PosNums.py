#POSITIVE NUMBERS IN A LIST OF RANGE

l1 = {1,0,4,-9,-43,-24,88,72,10}
print("Original list is:",l1)
print("Positive numbers in given list is: ")
for pos_numbers in l1:
    if pos_numbers>0:
        print(pos_numbers)

#OUTPUT:
#Original list is: {0, 1, 4, -24, 72, 10, -43, -9, 88}
#Positive numbers in given list is: 
#1
#4
#72
#10
#88