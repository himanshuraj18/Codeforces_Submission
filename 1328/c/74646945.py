import sys
for _ in range(int(sys.stdin.readline())):
	n=int(sys.stdin.readline())
	x=sys.stdin.readline()
	a='1'
	b='1'
	switch=False
	for i in range(1,n):
		if(switch==False):
			if(x[i]=='2'):
				a+='1'
				b+='1'
			elif(x[i]=='1'):
				a+='1'
				b+='0'
				switch=True
			else:
				a+='0'
				b+='0'
		else:
			if(x[i]=='2'):
				a+='0'
				b+='2'
			elif(x[i]=='1'):
				a+='0'
				b+='1'
			else:
				a+='0'
				b+='0'
	print(a)
	print(b)