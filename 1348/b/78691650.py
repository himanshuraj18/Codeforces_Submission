from sys import stdin
#from collections import Counter
#from math import ceil,log

def list_int():
	s=stdin.readline()[:-1]
	return list(map(int, s.split()))
def list_float():
	s=stdin.readline()[:-1]
	return list(map(float, s.split()))
def list_str():
	s=stdin.readline()[:-1]
	return list(s.split())
def space_int():
	s=stdin.readline()[:-1]
	return map(int, s.split())
def space_float():
	s=stdin.readline()[:-1]
	return map(float, s.split())
def space_str():
	s=stdin.readline()[:-1]
	return s.split()
def _int():
	s=stdin.readline()[:-1]
	return int(s)
def _str():
	s=stdin.readline()[:-1]
	return s
def _float():
	s=stdin.readline()[:-1]
	return float(s)
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
maxi=-(2**32)
mini=2**32
mod=10**9+7

#_______________________________________________________________________________________________________________________________________

for _ in range(_int()):
	n,k=space_int()
	l=list_int()
	s=list(set(l))
	if(len(s)>k):
		print(-1)
		continue
	a=s[:]
	for i in range(1,n+1):
		if(len(a)==k):
			break
		else:
			a.append(i)
	a.sort()
	ans=[]
	for i in range(n):
		for j in range(len(a)):
			ans.append(a[j])
	print(len(ans))
	print(*ans)