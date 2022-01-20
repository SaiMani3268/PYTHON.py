#CALCULATOR

print("CALCULATOR")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulo dividion")
print("6.power")

ch = int(input('Enter your choice:'))
  
if ch==1:
     a = int(input('Enter a:'))
     b = int(input('Enter b:'))
     c = a + b
     print(c)
elif ch==2:
    a = int(input('Enter a:'))   
    b = int(input('Enter b:'))
    c = a - b
    print(c)
elif ch==3:
    a = int(input('Enter a:'))
    b = int(input('Enter b:'))
    c = a * b
    print(c)
elif ch==4:
    a = int(input('Enter a:'))
    b = int(input('Enter b:'))
    c = a / b
    print(c)
elif ch==5:
    a = int(input('Enter a:'))
    b = int(input('Enter b:'))
    c = a % b
    print(c)
elif ch==6:
    a = int(input('Enter a:'))
    b = int(input('Enter b:'))
    c = a ** b
    print(c)
else:
    print("Invalid choice")
