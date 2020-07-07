from math import log2
for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	c=0
	for i in range(1,len(l)):
		if(l[i]<l[i-1]):
			c=max(c,int(log2(l[i-1]-l[i]))+1)
			l[i]=l[i-1]
	print(c)