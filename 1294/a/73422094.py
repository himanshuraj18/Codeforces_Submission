for _ in range(int(input())):
	a,b,c,n=map(int, input().split())
	m=max(a,b,c)
	a=m-a
	b=m-b
	c=m-c
	s=a+b+c
	if(s>n):
		print('NO')
	else:
		n=n-s
		if(n%3==0):
			print('YES')
		else:
			print('NO')