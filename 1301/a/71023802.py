for _ in range(int(input())):
	a=input()
	b=input()
	c=input()
	for i in range(len(a)):
		if(a[i]==c[i] or b[i]==c[i]):
			if(i==len(a)-1):
				print('YES')
		else:
			print('NO')
			break