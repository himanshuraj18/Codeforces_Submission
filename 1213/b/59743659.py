for _ in range(int(input())):
	n=int(input())
	l=list(map(int, input().split()))
	s=[l[0]]
	c=0
	for i in range(1,n):
		if(len(s)>0):
			while(len(s)!=0):
				if(l[i]<s[-1]):
					s.pop()
					c+=1
				else:
					s.append(l[i])
					break
			if(len(s)==0):
				s.append(l[i])
			elif(s[-1]!=l[i]):
				s.append(l[i])
		else:
			s.append(l[i])
	print(c)