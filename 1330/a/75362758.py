for _ in range(int(input())):
	n,x=map(int, input().split())
	l=list(map(int,input().split()))
	s=set(l)
	c=0
	f=False
	for i in range(1,101):
		if(i not in s):
			c+=1
		if(c==x):
			ans=i
			f=True
			break
	if(f):
		for i in range(ans+1,101):
			if(i in s):
				ans=i
			else:
				break
		print(ans)
	else:
		x=x-c
		ans=100+x
		print(ans)