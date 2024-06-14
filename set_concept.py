# a set is a keys without the values in the dictionary

x={"1","a","b",10,11,False,3.6} # the order is not concerened it always changes : it is a king of plastic bag
print(x)
x.add("d")
x.add("a") # same element can't be repeated
print(x)
x.remove(False)
print(x)
# x.pop() # random part will deleted
# print(x)
# x.pop()
# print(x)

x={1,2,3,4,"e","h","c"}
y={"a","b","c","d","e"}

print(x.intersection(y)) #order can be anything

print(x.union(y)) # considering all the elements in the y set and adding to the x set

print(x.difference(y)) # the elemtnts are only in x but not in y
print(y.difference(x)) # elements only in y but not in x
print(y-x) # same as differnce
print(list(x))
print(tuple(x))