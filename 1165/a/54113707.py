n,x,y=map(int, input().split())
s=input()
t=s[-x:]
a='0'*abs(x-y-1)+str(10**y)
#print(a)
#print(t)
ans=0
for i in range(len(a)):
	if(t[i]!=a[i]):
		ans+=1
print(ans)