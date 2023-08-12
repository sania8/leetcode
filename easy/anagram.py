def anagram(s,t):
    if(sorted(s)==sorted(t)):
        return True
    else:
        return False

s = input("Enter first string:")
t = input("Enter second string:")
ans = print(anagram(s,t))
