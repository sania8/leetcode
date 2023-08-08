#code to remove duplicates from a list
intial_list=[] 
n= int(input("enter the numbers to be append to list:"))
for i in range(n):
    x= int(input(f"enter {i+1}st number:"))
    intial_list.append(x)
unique_list=[]
for i in intial_list:
    if i not in unique_list:
        unique_list.append(i)
print("list with duplicates:" , intial_list)
print("list without duplicates:" , unique_list)