a = input("Enter the string:")
b = ' '.join(reversed(a.split()))
s=""
for i in range(len(b)):
    if b[i] == ' ':
        break
    s = b[:i+1]  # Extract the word before the space
l = len(s)
print(f'Length of {s} is:',l)

    

