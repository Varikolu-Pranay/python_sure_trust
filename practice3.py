# 2 friends are going out to eat, in total they have x money, they enter a restaurent and get a menu in form of a list (just the prices)
# we have to output the combination of two output that make the friends use all the money

x=180
menu=[10,20,60,40,30,200,100,80,140] # menu will always should be sorted if we go for binary search
y=None
done =False
for i in menu:
    y=x-i
    if y in menu:
        print(f"{i},{y}")
        
