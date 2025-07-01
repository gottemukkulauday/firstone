arr=[1,2,3,4,1,2,3,4,5,6,7,7,6,5,8,9]
print(arr)
n=len(arr)
m=0
for i in range(n):
    if(m<arr[i]):
        m=arr[i]

print(m)