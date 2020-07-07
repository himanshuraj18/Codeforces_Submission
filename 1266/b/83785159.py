t=int(input())
l=list(map(int, input().split()))
for i in range(t):
	n=l[i]
	if(1<=n%14<=6 and n//14>=1):
		print('YES')
	else:
		print('NO')