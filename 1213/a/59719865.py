n=int(input())
l=list(map(int, input().split()))
c1,c2=0,0
for i in range(n):
	if(l[i]%2==0):
		c1+=1
	else:
		c2+=1
print(min(c1,c2))