x=[i for i in range(1,11)]
print(x)
x=[2*i for i in range(1,11)]
print(x)

x=(i for i in range(1,11))  # this can be type casted into anything 
print(x)

x=list(i for i in range(1,11)) 
print(x)
x=tuple(i for i in range(1,11)) 
print(x)


x=list(int(input("hello :")) for i in range(1,11)) 
print(x)