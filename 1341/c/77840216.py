for _ in range(int(input())):
	n=int(input())
	l=list(map(int, input().split()))
	if(l==sorted(l) or l==sorted(l,reverse=True)):
		print('Yes')
	else:
		d={}
		for i in range(n):
			d[l[i]]=i
		s=set()
		f=True
		for i in range(1,n+1):
			if(i not in s):
				start=d[i]
				s.add(l[start])
				for j in range(start,n-1):
					s.add(l[j])
					if(l[j+1] in s):
						break
					if(l[j]+1!=l[j+1] and l[j+1] not in s):
						f=False
						break
			if(not f):
				break
		if(f):
			print('Yes')
		else:
			print('No')