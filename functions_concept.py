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
    

