t=int(input())
for _ in range(t):
	n,k=map(int, input().split())
	c=0
	while(n!=0):
		if(n%k==0):
			n//=k
			c+=1
		else:
			c+=(n%k)+1
			n//=k
	print (c-1)