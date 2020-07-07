n,m=map(int, input().split())
l=[{} for i in range(m)]
for i in range(n):
    s=list(input())
    for j in range(m):
        try:
            l[j][s[j]]+=1
        except:
            l[j][s[j]]=1
a=list(map(int, input().split()))
c=0
for i in range(m):
    c+=max(list(l[i].values()))*a[i]
print(c)