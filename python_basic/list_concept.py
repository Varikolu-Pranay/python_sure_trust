# x=(10)
# print(x,type(x)) # it consider it as integer
# x=(10,)
# print(x,type(x)) # it consider as tuple

#----------------list-----------------------# 

# x=["hi","my","name","is","..."]

# x.append("hello")
# print(x)
# y= x.pop() # the popped can bestores in a variable
# print(x)
# print(y)

# x.insert(4,"pranay")  # insert a value in a particular index /the inderx specifies the position of the added element
# print(x)

# x.insert(-1,"kumar") # len(x)-1 :the way it converts into positive using the formula
# print(x)

# y=x.pop()
# print(x)
# x.pop(2)
# print(x)

# x.remove("is")
# print(x)
# x.pop(x.index("hi")) # internal part od remove function

# x[-1]="varikolu" # it adds the element by deleteing that
# print(x)

# sentence ="__".join(x) # to convert from list to string
# print(sentence)

# print(sentence.split("__")) # string to a list

# sentence =list("Hello")
# print(" ".join(sentence))
# x=[1,2,3,4,5]
# sentence =str(x) # it considers as the  "[1,2,3,4,5]"
# print(sentence,type(sentence)) 
# print(sentence.split(","))

# x=input("enter 3 names : ")
# x=x.split(",")

# x[-2]="changed_name"
# y=x.pop()
# x.insert(1,y)
# x.append("new_name")
# x.pop(0)

# print(",".join(x))

# we can add two lists

x=[1,2,3,4,5]
y=[1,2,3,4,5]
print(x+y) # it concaonates
x.extend(y)
print(x)
x.append(y) # the entire list will be considered one element
print(x)
y.reverse()
print(y)
y.sort()
print(y) 

x=[1,3,4,5,6,7]*2
print(x) # 2 series will be printed
x=[1,2,3,4,5]+[1,2,3,4,5]
print(x)

#x=input()
y=[""]*30
y.append(x)
print(y)

