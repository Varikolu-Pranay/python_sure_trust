# print(2,3,"hello") # automatically space is allocated   
# print("hi","hello",sep='_')
# print("hi","hello",sep='\n')
# print("hi","hello",sep='_',end="")
# print("dog")
# print("hi","hello",sep='_',end="\n")
# print("dog")
f_name="pranay"
L_name="kumar"
full_name ="{} {}".format(f_name,L_name)
print("my name is "+f_name+ " "+L_name)
print("my name is ",f_name,L_name)
print("my name is {} {}".format(f_name,L_name))
print("my name is ",full_name)
# we can use f for Fstring 
print(f"my name is {f_name} {L_name}.")
print(f"my \nname is {f_name} {L_name}.")
print(f"my \tname i\bs {f_name} {L_name}.") #\b means back space
print(r"my name is {f_name} {L_name}.") # r is for raw string to print as it is

age=21
height="5'11''"
study="GCET"
Hobbies="chess"
achievement="certificate of best software developer training"
print(f"good evening all this is {full_name}.","My age is {} and {} tall.".format(age,height), "I am currently persuing my BTech at "+study,
      "comming to my hobbies i love to play {}.".format(Hobbies),"During my acedemics i received an "+achievement+"as one of my achievement" )

