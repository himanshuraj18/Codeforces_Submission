c=0
n,k=map(int,input().split())
l=list(map(int,input().split()))
l=l[0:n]
for i in range(0,n):
    if(l[k-1]<=l[i] and l[i]>0):
        c+=1
    else:
        break
print(c)