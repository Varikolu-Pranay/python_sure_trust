# molding the type of one thing
print(int(-6.7))
print(int(6.7))
print(int(True))
print(int("-87")+10) #we cant do float numbers

print(float(True))
print(float(4))
print(float("3.14")) # can convert decimal numbers from string to float 
print(float("3.14")+3.14)

print(str(91)) # prints in a form of a string
print(str(91.5))
x=str(65)
print(x,type(x))

x=bool(0)
print(x,type(x))
x=bool(4)
print(x,type(x)) # its a true because bool looks does the value have a negative or not if it has then its a true\
x=bool(-1)
print(x,type(x))
x=bool(0.00001)
print(x,type(x))
x=bool("")
print(x,type(x))


x=input("enter float input : ") # as input is considered as string
y=int(float(x))
z=str(y)
print(z,type(z))
print(z*5)

