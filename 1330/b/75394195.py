for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	m=max(l)
	s=set(l)
	if(m==len(s)):
		a1=l[:n-m]
		a2=l[n-m:]
		a3=l[:m]
		a4=l[m:]
		#print(a1,a2,a3,a4)
		s1=set(a1)
		s2=set(a2)
		s3=set(a3)
		s4=set(a4)
		f1=False
		f2=False
		if(len(s1)==max(a1) and len(s2)==max(a2) and max(a1)==n-m and max(a2)==m):
			f1=True
		if(len(s3)==max(a3) and len(s4)==max(a4) and max(a3)==m and max(a4)==n-m):
			f2=True
		if(f1==True and f2==True):
			if(n-m!=m):
				print(2)
				print(n-m,m)
				print(m,n-m)
			else:
				print(1)
				print(n-m,m)
		elif(f1==True):
			print(1)
			print(n-m,m)
		elif(f2==True):
			print(1)
			print(m,n-m)
		else:
			print(0)
	else:
		print(0)