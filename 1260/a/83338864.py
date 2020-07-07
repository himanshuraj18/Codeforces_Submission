n=int(input())
for _ in range(n):
	c,s=map(int, input().split())
	if(c==1):
		print(s*s)
	elif(s==1):
		print(1)
	else:
		if(s%c==0):
			print(c*((s//c)**2))
		else:
			a=s//c
			b=(s//c)+1
			bw=s%c
			aw=(c-bw)*a*a
			bw=bw*b*b
			print(aw+bw)
