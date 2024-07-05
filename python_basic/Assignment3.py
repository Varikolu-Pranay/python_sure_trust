# recreate functions on your own using loops
# sum,count,index take list as input

def Addition(list1):
    sum1=0
    for i in range(0,len(list1)):
        sum1+=list1[i]
    return sum1

def counting(N,get_list): # using the list1 extra because we can use any list rather from list1
    count=0
    for i in get_list:
        if i == N:
            count+=1
    return count

def Index(M,get_list):
    for i in range(0,len(get_list)):
        if get_list[i] == M:
            return f"Index : {i}"
            break
    return f"{M} is not in the list"


# n=int(input("Enter the size of the list : "))
# list1=list(int(input(f"Enter element {i} : ")) for i in range(1,n+1))

list1=list(map(int,input("Enter the elements seperated with (,)").split(',')))
print(list1)

 
sum_list=Addition(list1)
print(f"Sum of elements in the list : {sum_list}")

a=set(list1)
for i in a:
    print(f"{i} :repeated {counting(i,list1)} times")

list2=[1,2,3,4]
print(f"count : {counting(2,list2)}")


index_list=Index(9,list1)

print(index_list)

k=int(input("Enter the element to find out the index : "))
print(Index(k,list1))








