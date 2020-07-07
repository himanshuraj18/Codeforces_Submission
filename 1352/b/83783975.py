from sys import stdin
# from collections import Counter
# from math import ceil,log

# def gcd(a, b):
# 	if(a==0):
# 		return b 
# 	return gcd(b%a,a)

# def sieve(n): 
# 	prime=[True for i in range(n+1)]
# 	p=2
# 	while(p*p<=n): 
# 		if (prime[p]==True): 
# 			for i in range(p*p,n+1,p): 
# 				prime[i]=False
# 		p+=1
# 	prime[0]=False
# 	prime[1]=False
# 	return prime 

# alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# mod=10**9+7

input=stdin.readline

def list_input():
	return list(map(int, input().split()))

def sep_input():
	return map(int, input().split())

#_______________________________________________________________________________________________________________________________________

for _ in range(int(input())):
	n,k=sep_input()
	if((n%2==1 and k%2==0) or n<k):
		print('NO')
	elif(n==k):
		print('YES')
		print('1 '*k)
	else:
		a=n//k
		b=n%k
		if(b==0):
			print('YES')
			print((str(a)+" ")*k)
			continue
		c1=n//k
		c2=(n//k)+1
		nc1=k-b
		nc2=b
		#print(c1,c2,nc1,nc2)
		if(nc1%2==1 and nc2%2==1):
			print('NO')
			continue
		elif(nc2%2==0):
			print('YES')
			ans=((str(c1)+" ")*nc1)+((str(c2-1)+" ")*(nc2//2))+((str(c2+1)+" ")*(nc2//2))
			print(ans)
		elif(c1==1):
			print('NO')
		elif(nc1%2==0):
			print('YES')
			ans=((str(c2)+" ")*nc2)+((str(c1-1)+" ")*(nc1//2))+((str(c1+1)+" ")*(nc1//2))
			print(ans)