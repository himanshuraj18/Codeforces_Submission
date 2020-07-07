for _ in range(int(input())):
	l=list(map(int, input().split()))
	n=l[0]
	k=l[1]
	if(n%k==0):
		print(n)
		continue
	a=n//k
	b=(n//k)+1
	na=k-n%k
	nb=n%k
	#print(a,b,na,nb)
	if(nb>k//2):
		na=na+nb-(k//2)
		nb=(k//2)
	print(nb*b+na*a)