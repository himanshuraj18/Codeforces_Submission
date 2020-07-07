for _ in range(int(input())):
	s=input()
	z=s.count('0')
	c=0
	f1=0
	f2=0
	for i in range(len(s)):
		c+=int(s[i])
		if(int(s[i])%2==0 and int(s[i])!=0):
			f1=1
		elif(int(s[i])==0):
			f2=1
	if(c%3==0 and f1==1 and z>0):
		print('red')
	elif(c%3==0 and f2==1 and z>1):
		print('red')
	else:
		print('cyan')