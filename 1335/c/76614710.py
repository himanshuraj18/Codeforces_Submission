from collections import Counter
for _ in range(int(input())):
	n=int(input())
	l=list(map(int, input().split()))
	s=set(l)
	dis=len(s)
	if(n==1):
		print(0)
		continue
	elif(n==2 or dis==n):
		print(1)
		continue
	dis=dis-1
	d=Counter(l)
	m=max(list(d.values()))
	if(dis>=m):
		print(m)
	elif(dis<m):
		if(m-dis==1):
			print(dis)
		else:
			print(dis+1)
