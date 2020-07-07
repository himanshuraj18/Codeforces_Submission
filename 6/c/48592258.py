n=int(input())
l=list(map(int, input().split()))
if(n==1):
	print(1,0)
elif(n==0):
	print(0,0)
else:
	a,b,i,j=0,0,0,n-1
	ascore=0
	bscore=0
	while i<=j:
		if(ascore+l[i]>bscore+l[j]):
			b+=1
			bscore+=l[j]
			j-=1
		elif(ascore+l[i]<bscore+l[j]):
			a+=1
			ascore+=l[i]
			i+=1
		else:
			if(i==j or i+1==j):
				a+=1
				ascore+=l[i]
				i+=1
			elif(i!=j):
				a+=1
				ascore+=l[i]
				b+=1
				bscore+=l[j]
				i+=1
				j-=1
	print(a,b)