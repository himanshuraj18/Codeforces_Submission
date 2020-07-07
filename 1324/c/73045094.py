for _ in range(int(input())):
	s=input()
	n1=len(s)
	s='R'+s+'R'
	n=len(s)
	l=[]
	for i in range(n):
		if(s[i]=='R'):
			l.append(i)
	if(len(l)==2):
		print(n1+1)
	else:
		c=0
		for i in range(1,len(l)):
			if(l[i]-l[i-1]>c):
				c=l[i]-l[i-1]
		print(c)