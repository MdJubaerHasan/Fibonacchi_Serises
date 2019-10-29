n = input('Enter number: ')
flag = 0
n = int(n)
for i in range(2,(n//2),1):
    if n%i==0:
        flag=1
if flag==0:
    print("prime")
else:
    print("Not Prime")