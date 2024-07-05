# used to create files in python
# creating                 CRUD
# retreiving
# updating
# deleting 
# x is used to create a file
# w is for writing
# r is to read the file
# a is used to append
try:
    file =open("Attendence.txt","x") # if present it will open or it will creaate new one
    file.close
except FileExistsError:
    pass
file = open("Attendence.txt","w")
#file.write("names,days_present\n")
    
attende={
    "pranay" : 5,
    "bhalu" : 6,
    "Hari" : 5
}

data=[]
for key in attende:
    data.append(f"{key},{attende[key]}")
# file.write("Pranay\n")
#file.writelines(["hello,4\n","hi,5\n"])
file.write("\n".join(data))
file.close()

# appending data, using write function it will overwrite the data

name="josh"
days=3
# with open("Attendence.txt","w") as file:
#     data.append(f"{name}, {days}")
#     file.write("\n".join(data))
with open("Attendence.txt","a") as file:
    file.write(f"\n{name},{days}")

new_data=[]
with open("Attendence.txt","w+") as file:
    old_data= file.read().split("\n")
   

    for line in old_data:
        print(line.split(","))
        line[1]=str(int(line[1])+1)
        print(line)






# # reading data
# with open("Attendence.txt","r") as file:
#     data=file.read()
# print(data)

# with open("Attendence.txt","r") as file:
#     data=file.readlines(10) # give the characters of a single line 
# print(data)

