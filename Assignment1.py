
name=input("Enter your name : ")
height=input("Enter your Height in Meters : ")
weight=input("Enter your weight in Kilograms : ")


if height == "":
    height=0
else:
    height=float(height)

if weight == "":
    weight=0
else:
    weight=float(weight)

# Metric system
if name =="":
    name="Anonymous"

if height == 0 and  weight == 0 :
    print("Height and weight both are not defined")
elif height == 0 :
    print("Height is not defined")
elif weight == 0 :
    print("Weight is not defined")


if height !=0  and  weight !=0 :
    BMI=float(weight/pow(height,2))
    if BMI <18.5:
        condition="Underweight"
    elif BMI>=18.5 and BMI<= 24.9:
        condition="Healthy weight"
    elif BMI>=25.0 and BMI<= 29.9:
        condition="Overweight"
    elif BMI >= 30.0:
        condition="Obesity"
    print(f"{name} you are under {condition} category with BMI of {BMI}")
