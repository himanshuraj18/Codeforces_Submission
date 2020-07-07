for _ in range(int(input())):
	n,k=map(int, input().split())
	l=list(map(int, input().split()))
	l.sort()
	if(l[0]+2*k<l[-1]):
		print(-1)
	else:
		print(l[0]+k)