x={                       #keys can be tuple can't be list
    "name" : "pranay",
    2:False,
    True:4.5,
    None:[3,2,3,4],
    (2,3):"hi"
}
print(x,type(x))
print(x[True])

# adding an element can be done at last
x[4.55]="kumar"
x[True]="hello" # to change the values using key
y= x.pop(2) #using key value
print(x)
print(y) # returned pop value only value will be printed

#----- CRUD : creating,retreiving, updating, deleting

print(list(x.keys())) # type casting into list
print(list(x.values()))
print(x.keys()) # type casting into list
print(x.values())


y=x.pop(5, "not found") # this can also happen without the declared elements
print(y)
print(list(x.items()))

print(list(x)) # if we type cast into list then only keys will be printed

# y=x.copy() # any cahnges to x will be not refelected into y
# y=x # channges will change into y also

Y=x.get(10) # if key is not found return NONE, 
Y=x.get(10,"return") # insted of none it returns the return 
print(Y)

x[None].append("new")

  



info={
    "name" :{
        "first" : "pranay",
        "last"  : "kumar"
    }
}


print(info["name"]["first"])

# use user input to fill a dictionary called "info" which is well thought out and specific data is stored seperately
# later populate the dictionary with user inpu

info1={
    "name": {
        "first" : "",
        "last" : ""

    },
    "contacts":{
        "phonenumber": "",
        "emailid" :""
    },
    "weight": "",
    "height": "",
    "location" :""
}

info1["name"]["first"]=input("enter your first name :")
info1["name"]["last"]=input("enter your last name :")
info1["contacts"]["phonenumber"]=input("enter your phone number :")
info1["contacts"]["emailid"]=input("enter your emailid :")
info1["weight"]=float(input("enter your weight :"))
info1["height"]=float(input("enter your height in (m) :"))
info1["location"]=input("enter your location :")

print(info1)


