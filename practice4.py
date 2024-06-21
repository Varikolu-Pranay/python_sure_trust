def add_user(name: str,atten: int,filename):
    














file =open("attendence.txt","x") 
file.close()
file = open("Attendence.txt","w")

    
attende={
    "pranay" : 5,
    "bhanu" : 6,
    "Hari" : 5
}

data=[]
for key in attende:
    data.append(f"{key},{attende[key]}")

add_user("pavan",7,file)

