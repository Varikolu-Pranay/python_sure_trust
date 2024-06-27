def add_user(name: str,atten: int):
    with open("Attendence.txt","a") as file:
        file.write(f"\n{name},{atten}")
    

def pop_user(name: str):
    new_data=[]
    with open("Attendence.txt","r") as file:
        old_data=file.read().split("\n")
        new1=dict(old_data)

    print(new1)


try:
    file =open("Attendence.txt","x") 
    file.close()
  
except FileExistsError:
    pass
file = open("Attendence.txt","w")

    
attende={
    "pranay" : 5,
    "bhanu" : 6,
    "Hari" : 5
}

data=[]
for key in attende:
    data.append(f"{key},{attende[key]}")
file.write("\n".join(data))

file.close()

add_user("pavan",7)
pop_user("pranay")

