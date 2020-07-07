from math import ceil
for _ in range(int(input())):
	n,k=map(int, input().split())
	l=list(map(int, input().split()))
	p=[0 for i in range(n)]
	for i in range(1,n-1):
		if(l[i]>l[i+1] and l[i]>l[i-1]):
			p[i]=1
	a=[]
	c=0
	for i in range(n):
		c+=p[i]
		a.append(c)
	m=a[k-2]-a[0]
	a1=0
	#print(a)
	for i in range(1,n-k+1):
		temp=a[i+k-2]-a[i]
		#print(temp)
		if(temp>m):
			m=temp
			a1=i
	print(m+1,a1+1)