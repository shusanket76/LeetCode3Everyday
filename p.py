a = [1,2,3,4,5,6,7,8]
temp = a[0]
for x in range(1,len(a)):
    temp2 = a[x]
    a[x] = temp
    temp=temp2

print(a)