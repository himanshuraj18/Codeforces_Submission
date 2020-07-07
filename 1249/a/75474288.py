for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	l.sort()
	f=False
	for i in range(1,n):
		if(l[i]-l[i-1]==1):
			f=True
			break
	if(f):
		print(2)
	else:
		print(1)