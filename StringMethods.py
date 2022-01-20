#STRING METHODS
#Used strings are text1........text15 and a tuple named fruitss

text1 = "hi,this is someone,you haven't known till now!!!"
text2 = "Hello,World!!"
text3 = "sk𐌙 is blue"
text4 = "P\tYT\tHO\tN"
text5 = "I am {age} years old"
text6 = "robot5"
text7 = "56"
text8 = "\u0030"
text9 = "\u0047"
text10 = "demo21"
text11 = "21demo"
text12 = " "
fruits = ("apple","banana","orange","kiwi")
text13 = "     not always    "
text14 = "one plus one is two,one minus one is zero"
text15 = "Thank you for the music\nWelcome to the jungle"

#capitalize()=Converts the first character to upper case
x=text1.capitalize()
print(x)

#casefold()=Converts string into lower case
x=text2.casefold()
print(x)

#center()=Returns a centered string
x=text2.center(23,"*")
print(x)

#count()=returns no. of times specified value occurs in a string
x=text1.count("i")
print(x)

#encode()=Returns an encoded version of the string
print("ENCODING CONTAINS 5 TYPES OF PARAMETERS")
print(text3.encode(encoding="ascii",errors="backslashreplace"))
print(text3.encode(encoding="ascii",errors="ignore"))
print(text3.encode(encoding="ascii",errors="namereplace"))
print(text3.encode(encoding="ascii",errors="replace"))
print(text3.encode(encoding="ascii",errors="xmlcharrefreplace"))

#endswith()=Returns true if  -the string ends with the specified value
x=text2.endswith("!")
print(x)

#expandtabs()=Sets the tab size of the string
x=text4.expandtabs()
print(x)

#find()=Searches the string for a specified value and returns the position of where it was found
x=text3.find("i")
print(x)

#format()=formats specified values in a string
x=text5.format(age=18)
print(x)

#index()=returns position of specified value
x=text1.index('y')
pritn(x)

#isalnum()=returns true if all characters are alphanumeric
x=text6.isalnum()
print(x)

x=text6.isalpha()
print(x)

x=text6.isdigit()
print(x)

x=text7.isdigit()
print(x)

x=text8.isdigit()
print(x)

x=text8.isdecimal()
print(x)

x=text9.isdecimal()
print(x)

x=text10.isidentifier()
print(x)

x=text11.isidentifier()
print(x)

x=text1.islower()
print(x)

x=text7.isnumeric()
print(x)

x=text8.isnumeric()
print(x)
 
x=text1.isprintable()
print(x)

x=text4.isprintable()
print(x)

x=text12.isspace()
print(x)

#istitle()=all words in a text start with an upper case and the should be small
x=text2.istitle()
print(x)

x=text4.isupper()
print(x)

#join()=specified value is joined after every string
x="@".join(fruits)
print(x)

#ljust()=adds a string that is specified until specified position is
reached
x=text2.ljust(18,"-")
print(x,text3) 

x=text4.lower()
print(x)

#lstrip()=removes all the left side characters of specified string
x=text13.lstrip()
print(text2,x,text3)

#maketrans()=replaces mentioned with specified value
x=text3.maketrans(lueb,lueg)
print(text3.translate(x))

#partition()=Returns a tuple where the string is parted into three parts
x=text1.partition("you")
print(x)

x=text14.replace("one","three",2)
print(x)

#rfind()=finds last position of specified string,if not -1,also finds b/w 2 specified positions
x=text5.rfind("a",5,10)
print(x)

#rindex()=same as rfind() but raise an exception when specified value is not found

#rjust(),rpartition(),rstrip() works similar to those with l except that right instead left

x=text1.rsplit(",",1)
prit(x)

x=text1.split(",",1)
prit(x)

#strip()=trims both sides

x=text3.upper()
print(x)

x=text15.splitlines()
print(x)

x=text3.startswith("b",7,9)
print(x)

x=text2.swapcase()
print(x)

x=text5.title()
print(x)

#zfill()=Fills the string with a specified number of 0 values at the beginning
x=text6.zfill(15)
print(x)



#OUTPUT:
#Hi,this is someone,you haven't known till now!!!
#hello,world!!
#*****Hello,World!!*****
#4
#ENCODING CONTAINS 5 TYPES OF PARAMETERS
#b'sk\\U00010319 is blue'
#b'sk is blue'
#b'sk\\N{OLD ITALIC LETTER KHE} is blue'
#b'sk? is blue'
#b'sk𐌙 is blue'
#True
#P       YT      HO      N
#4
#I am 18 years old
#19
#True
#False
#False
#True
#True
#True
#True
#True
#False
#True
#False
#True
#True
#True
#True
#False
#True
#True
#True
#apple@banana@orange@kiwi
#Hello,World!!----- sk𐌙 is blue
#p	yt	ho	n
#Hello,World!! not always      sk𐌙 is blue
#sk𐌙 is glue
3('hi,this is someone,', 'you', " haven't known till now!!!")
#three plus three is two,one minus one is zero
#-1
#['hi,this is someone', "you haven't known till now!!!"]
#['hi', "this is someone,you haven't known till now!!!"]
#SK𐌙 IS BLUE
#['Thank you for the music', 'Welcome to the jungle']
#True
#hELLO,wORLD!!
#I Am 18 Years Old
#000000000robot5


