n=int(input())
l=list(map(int, input().split()))
a=[l[0]]
m=l[0]
for i in range(1,n):
    a.append(l[i]+m)
    if(a[-1]>m):
        m=a[-1]
print(*a)