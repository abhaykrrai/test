n = (input("enter a string"))
s=''
for i in n:
    if ord(i)==32:
        continue
    else:
        s+=i
print(s)
