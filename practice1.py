#print mean median mode of any numerrical list

n=int(input("Enter number of elements in the list : "))
x=list(int(input(f"Enter element {i} : ")) for i in range(1,n+1))


mean =sum(x)/len(x)
print(f"mean : {mean}")

x1=sorted(x)
#print(x1)
if len(x1) %2 ==1:
    print(f"Median : {x1[len(x1)//2]}")
else:
    print(f"Median : {(x1[len(x1)//2] + x1[(len(x1)//2)-1])/2}")

unique_x =set(x)
highest_frequency=0
value=None


for el in unique_x:
    freq=x.count(el)
    

    if( freq>highest_frequency):
        highest_frequency=freq
        value=el

print(f"Mode : {value}")

# Another method for mode 
# counter={}
# for el in x:
#     if el in counter:
#         counter[el]+=1
#     else:
#         counter[el]=1

# print(counter)
# highest_freq =0
# mode=[]
# for el in counter:
#     if counter[el] > highest_freq:
#         highest_freq=counter[el]
#         mode=el
#     elif counter[el] == highest_freq:
#         mode.append(el)


