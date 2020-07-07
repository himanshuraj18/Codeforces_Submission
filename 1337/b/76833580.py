for _ in range(int(input())):
	x,n,m=map(int, input().split())
	for i in range(n):
		if(x>20):
			x=(x//2)+10
		else:
			break
	for i in range(m):
		x=x-10
	if(x<=0):
		print('YES')
	else:
		print('NO')