for _ in range(int(input())):
	n=int(input())
	a=list(map(int, input().split()))
	b=list(map(int, input().split()))
	if(a[0]!=b[0]):
		print('NO')
		continue
	try:
		pos=a.index(1)
	except:
		pos=-1
	try:
		neg=a.index(-1)
	except:
		neg=-1
	ans=True
	for i in range(1,n):
		if(a[i]>b[i]):
			if(neg>=i or neg==-1):
				ans=False
				break
		elif(a[i]<b[i]):
			if(pos>=i or pos==-1):
				ans=False
				break
	if(ans):
		print('YES')
	else:
		print('NO')