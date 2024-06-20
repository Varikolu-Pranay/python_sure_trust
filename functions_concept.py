# def func() -> None:  # this function is not used to return anything(just for redability)
#     return 5
# print(func())

#def func() -> Int:  # if we retun string of input string it does not care 

def fun(x,y):
    return "Hello"

    # return None  It automatically dones 

print(type(fun(1,2))) # it give output type as string


def get_full_name(first_name= None,middle_name=None,last_name=None):
    full_name=""
    if first_name:
        full_name+=first_name
    if middle_name:
        full_name+=middle_name
    if last_name:
        full_name+=last_name
    return full_name
    

x=5
def change():
    x=3   # this is only in this scope and return is not stored in the function call
    return x
print(x)

change()
print(x)


x=5
def change():
    global x # this make changes
    x=3
    return x
print(x)

change()
print(x)


x=[1,2,3]
def change():
    x.append(5) # if there is no variable declared in local scope it checks in global scope
change()
print(x)



x=[1,2,3]
def change():
    x=[]
    x.append(5) # no change in global variable
change()
print(x)


x=5
def change(y):
    y+=3
change(x)
print(x)

