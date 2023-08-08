initial_list = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    x = int(input(f"Enter {i+1}st number: "))
    initial_list.append(x)
unique_list = []
for i in initial_list:
    if initial_list.count(i) == 1 and i not in unique_list:
        unique_list.append(i)
print("entered list:" , initial_list)
print("Numbers that are not duplicated:", unique_list)
