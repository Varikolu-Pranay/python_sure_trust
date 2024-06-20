# print(type(Exception))

# age=input("enter your age:" )

# if age:
#     age=int(age)
# else:
#     print("Bad input")

                                 # for strings it throws error in any condition
# print("Doing something")

# instead 

# age=input("enter your age:" )

# try:
#     age=int(age)
#     age=age/0
# except Exception as error:
#     print("Bad input",error)



# x=[2,4,2,5,7,8,4,3,7,0]

# x_dict ={}

# for el in x:
#     try:
#         x_dict[el]+=1
#     except:
#         x_dict[el] =1

# print(x_dict)






# age=10

# try:
#     age=int(age)
#     age=age/0
# except ValueError:
#     print("Value error")
# except TypeError:
#     print("Type error")
# except Exception as e:
#     print(f"{e}")




# print("Doing something")

# try:
#     y
# except Exception as e:  # name not defined error
#     print(e)

# x=[2,3,4,6,7,8,4]
# roll=15        # list index out of range
# try:
#     print(f"Marks for roll no. {roll} are {x[roll-1]}")
# # except Exception as e:
# #     print(e)

# except IndexError:
#     print(f"The class only has {len(x)} no of students")


# x=[2,3,4,6,7,8,4]
# roll=input("Enter Roll no : ")
# try:
#     roll =int(roll)
#     print(f"Marks for roll no. {roll} are {x[roll-1]}")
# # except Exception as e:
# #     print(e)
# except ValueError:
#     print("value error")

# except IndexError:
#     print(f"The class only has {len(x)} no of students")

# KeyboardInterrupt error occurs when ever we press Ctrl C in keybord while typing an input 


x=[2,3,4,6,7,8,4]
roll=input("Enter Roll no : ")

while True:
    try:
        roll =input("Enter roll no. ")
        roll =int(roll)
        marks =x[roll-1]
        break
    except KeyboardInterrupt:
        print("Bad input")
        roll=1
        marks=x[roll]
        break
    except ValueError:
        print("value error")

    except IndexError:
        print(f"The class only has {len(x)} no of students")

    except Exception as e:
        print(f"unknown error : {e}")
    







