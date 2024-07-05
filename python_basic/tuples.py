new1 =("de","m","fd","he","da")
# tuples can't be modified / imutable
print(new1[len(new1)-1])
print(new1[-3])
print(new1.index("de"))
print(new1.count("da"))

x,y,z=1,2,3  # if there is comma's in the code it understands as tupple
co_ordinates=y,x,y,x,z

x=5   # x value will not be chnaged in the tuple
print(x)

print(co_ordinates)
print(sum(co_ordinates)) # only numerical tuples can be added not strings

new2 =("su","mn",True,("sa","kl",(3,4,1),"jl"),"tue",1,"wed")
print(new2[3])
print(new2[-4][1])
print(new2[-4] [2][1])
