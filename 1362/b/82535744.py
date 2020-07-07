from sys import stdin
# from collections import Counter
from math import log

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

def list_input():
	return list(map(int, input().split()))

def sep_input():
	return map(int, input().split())

#_______________________________________________________________________________________________________________________________________

for _ in range(int(input())):
	n=int(input())
	l=list_input()
	if(n%2==0):
		s=set(l)
		ff=0
		for j in range(1,1025):
			f=1
			for i in range(n):
				if(l[i]^j not in s):
					f=0
					break
			if(f==1):
				print(j)
				ff=1
				break
		if(ff==0):
		    print(-1)
	else:
		print(-1)
