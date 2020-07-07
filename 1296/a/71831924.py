for _ in range(int(input())):
	n=int(input())
	a=list(map(int, input().split()))
	c=0
	for i in range(n):
		if(a[i]%2==1):
			c+=1
	if(c==n):
		if(n%2==0):
			print('NO')
		else:
			print('YES')
	elif(c==0):
		print('NO')
	else:
		print('YES')