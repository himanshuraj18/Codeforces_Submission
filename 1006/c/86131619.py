import sys
# from collections import deque
# from collections import Counter
# from math import sqrt
# from math import log
# from math import ceil
# from bisect import bisect_left, bisect_right

# alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# mod=10**9+7
# mod=998244353

# def BinarySearch(a,x): 
# 	i=bisect_left(a,x) 
# 	if(i!=len(a) and a[i]==x): 
# 		return i 
# 	else: 
# 		return -1

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
# 	s=set()
# 	for i in range(len(prime)):
# 		if(prime[i]):
# 		s.add(i)
# 	return s

# def gcd(a, b):
# 	if(a==0):
# 		return b 
# 	return gcd(b%a,a)

fast_reader=sys.stdin.readline
fast_writer=sys.stdout.write

def input():
	return fast_reader().strip()

def print(*argv):
	fast_writer(' '.join((str(i)) for i in argv))
	fast_writer('\n')

#____________________________________________________________________________________________________________________________________

for _ in range(1):
	n=int(input())
	l=list(map(int, input().split()))
	pref1=[0 for i in range(n)]
	pref2=[0 for i in range(n)]
	c1=0
	c2=0
	for i in range(n):
		c1+=l[i]
		c2+=l[n-i-1]
		pref1[i]=c1
		pref2[n-i-1]=c2
	i=0
	j=n-1
	maxs=0
	while(i<j):
		#print(i,j,pref1[i],pref2[j])
		if(pref1[i]==pref2[j] and maxs<pref1[i]):
			maxs=pref1[i]
		if(pref1[i]==pref2[j]):
			i+=1
			j-=1
		elif(pref1[i]>pref2[j]):
			j-=1
		else:
			i+=1
	print(maxs)