for _ in range(int(input())):
	a,b=map(int, input().split())
	if(a%b==0):
		print(0)
	else:
		m2=b-(a%b)
		print(m2)