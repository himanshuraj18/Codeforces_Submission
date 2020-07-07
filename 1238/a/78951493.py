from sys import stdin
#from collections import Counter
#from math import ceil,log

def _gcd(a, b):
	if(a==0):
		return b 
	return _gcd(b%a,a)
def _sieve(n): 
	prime=[True for i in range(n+1)]
	p=2
	while(p*p<=n): 
		if (prime[p]==True): 
			for i in range(p*p,n+1,p): 
				prime[i]=False
		p+=1
	prime[0]=False
	prime[1]=False
	return prime 

alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums=[0,1,2,3,4,5,6,7,8,9]
mod=10**9+7
input=stdin.readline

#_______________________________________________________________________________________________________________________________________

for _ in range(int(input())):
	x,y=map(int, input().split())
	if(x-y<2):
		print('NO')
	else:
		print('YES')
