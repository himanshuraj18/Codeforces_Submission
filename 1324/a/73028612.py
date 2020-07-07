for _ in range(int(input())):
	n=int(input())
	l=list(map(int, input().split()))
	c=l[0]%2
	f=True
	for i in range(1,n):
		if(l[i]%2!=c):
			print('NO')
			f=False
			break
	if(f):
		print('YES')