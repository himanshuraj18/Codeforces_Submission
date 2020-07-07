for _ in range(int(input())):
	n,m=map(int, input().split())
	a=list(map(int, input().split()))
	p=list(map(int, input().split()))
	s=set(p)
	l=sorted(a)
	f1=True
	for j in range(n):
		f=True
		for i in range(n-1):
			if(a[i]>a[i+1]):
				f=False
				if(i+1 in s):
					a[i],a[i+1]=a[i+1],a[i]
		if(f):
			print('YES')
			f1=False
			break
	if(f1):
		print('NO')