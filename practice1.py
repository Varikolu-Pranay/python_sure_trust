x=[2,4,5,2,6,7,3,6,1,3,3,8]

mean =sum(x)/len(x)
print(mean)

x1=sorted(x)
print(x1)
if len(x1) %2 ==1:
    print(x1[len(x1)//2])
else:
    print((x1[len(x1)//2] + x1[len((x1//2)+1)]/2))

unique_x =set(x)
highest_frequency=0
for el in unique_x:
    freq=x.count(el)

    if( freq>highest_frequency):
        highest_frequency=freq


