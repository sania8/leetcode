# Program to find out the missing number 
x=[1,0,3,-1] #intialising the array any example can be given
b = len(x)
missing=[]
for i in range(b):
    if(i not in x and i>0):
        missing.append(i)
for i in missing:
    print("The missing number is:",i)