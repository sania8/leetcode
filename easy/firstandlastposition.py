x=[]
n = int(input("enter the Range:"))
print(f"enter the {n} elements in the list")
for i in range(n):
    a = int(input(""))
    x.append(a)
print(x)
found=[]
target = int(input("enter the element you want to search:"))
for i in range(len(x)):
    if(x[i]==target):
        found.append(i)
if found:
        print([found[0], found[-1]])
else:
        print([-1,-1])