x=[2,4,6,8,10,12,14,16,18,20]

print(x[3:8]) # 3 to 8-1 index elements are teken 
x=x[2:8]
print(x)

print(x[2:]) # 2 to the last same as vice versa
print(x[1:-3])
print(x[1: :2])
print(x[5:0:-1]) # to reverse the list  .reverse function

x=[1,2,3,4,5,["hi","hello","join"],6,7,8]
print(x[5][0:2]+x[1:2])

print(list(range(1,10,2)))# to get a elements in the range specified with a step

#------------Table of 5

print(list(range(5,51,5)))

# take a number as user input print out the table of that number

x=int(input("Enter number"))
#print(list(range(x,(x*10)+1,x)))
z=int(input("enter the range"))

y=list(range(0,x*z+1))
print(y[x:x*z+1:x])

# initialize a list with a size so that we can save the memory and time to append