
f_name=input("first name :")
full_name=input("full name :")
# print(f"{f_name} {l_name}")
# print(f"{f_name} {type(l_name)}") # basically input return a string /or default data type is string
age=input(f"{full_name} Enter your age: ")
height=input("enter your height: ")
study=input("enter your college name: ")
Hobbies=input("enter you top most priority hobby: ")
achievement=input("Express your best achievement: ")
print(f"good evening all this is {full_name}.","My age is {} and {} tall.".format(age,height), "I am currently persuing my BTech at "+study,
      "comming to my hobbies i love to play {}.".format(Hobbies),"During my acedemics i received an "+achievement+"as one of my achievement" )
