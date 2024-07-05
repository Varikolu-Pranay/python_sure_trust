dict1={}
n=1
while(n<10):
    number=int(input("Enter the number : "))

    if number in dict1.keys():
        value=dict1.get(number)
        dict1[number]=value+1
    else:
        dict1[number] =1
    n+=1

print(dict1)

