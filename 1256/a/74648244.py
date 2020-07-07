for _ in range(int(input())):
	a,b,n,s=map(int, input().split())
	if(a*n>=s):
		if(s%n<=b):
			print('YES')
		else:
			print('NO')
	else:
		if(b+n*a>=s):
			print('YES')
		else:
			print('NO')