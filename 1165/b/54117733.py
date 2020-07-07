n=int(input())
l=list(map(int, input().split()))
l.sort()
#print(l)
ans=0
k=1
for i in range(n):
	if(l[i]>=k):
		ans+=1
		k+=1
		#print(l[i])
print(ans)