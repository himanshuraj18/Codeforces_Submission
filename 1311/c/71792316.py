for _ in range(int(input())):
	n,m=map(int, input().split())
	s=input()
	a=[0 for i in range(26)]
	p=list(map(int, input().split()))
	p.append(len(s))
	l=[0 for i in range(len(s))]
	for i in range(len(p)):
		l[p[i]-1]+=1
	#print(l)
	m=0
	for i in range(len(l)-1,-1,-1):
		m+=l[i]
		#print(m)
		l[i]=m
	#print(l)
	for i in range(len(s)):
		c=ord(s[i])-97
		a[c]+=l[i]
	print(*a)