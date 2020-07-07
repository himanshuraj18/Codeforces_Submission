for _ in range(int(input())):
	n,x=map(int,input().split())
	l=list(map(int,input().split()))
	l.sort()
	if(l[-1]==x):
		print(l.count(x))
	elif(l[-1]<x):
		print(0)
	else:
		a=l[::-1]
		s=0
		c=0
		for i in range(n):
			a[i]=a[i]-x
		for i in range(n):
			if(s+a[i]<0):
				break
			else:
				s=s+a[i]
				c+=1
		print(c)