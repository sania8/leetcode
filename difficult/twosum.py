x = int(input("Enter the range:"))
l=result=[]
for i in range(x):
    a = int(input(f"Enter {i+1}st element:"))
    l.append(a)
print("Entered list:" , l)

num = int(input("Enter the number:"))
for i in range(0,len(l)):
    for j in  range(i+1,len(l)):
        if(l[i]+l[j]==num):
            result = [i,j]
print(f"The numbers in the list which gives {num} is:" , result)
