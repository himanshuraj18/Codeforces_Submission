n,l,r=map(int , input().split())
li=[]
for i in range(0,21):
	li.append(2**i)
if(n==1):
	print(1,1)
elif(r==1):
	print(n,n)
elif(l==n):
	print(sum(li[:n]),sum(li[:n]))
else:
	if(l==1):
		mini=n
	else:
		mini=sum(li[:l])+(n-l)
	if(r==n):
		maxi=sum(li[:n])
	else:
		maxi=li[r-1]*(n-r+1)+sum(li[:r-1])
	print(mini,maxi)