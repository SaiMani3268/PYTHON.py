#FIBONACCI SERIES

nterms = int(input('Enter number of terms:'))
n1 = 0
n2 = 1
count = 0
if nterms<=0:
    print("Please enter positive number")
elif nterms==1:
    print("Fibonacci series for 1 term is:")
    print(n1)
else:
    print("Fibonacci Series is:")
    while count<nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count = count +1

#OUTPUT:
#Enter number of terms:6
#Fibonacci Series is:
#0
#1
#1
#2
#3
#5