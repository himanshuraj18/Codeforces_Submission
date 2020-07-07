import sys
from collections import deque
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
	s=input()
	n=len(s)
	l=[]
	for i in range(n):
		if(ord(s[i])<=90):
			l.append(0)
		else:
			l.append(1)
	if(l.count(0)==n or l.count(1)==n):
		print(0)
		break
	first_one=-1
	last_zero=-1
	for i in range(len(l)):
		if(first_one==-1 and l[i]==1):
			first_one=i
		if(l[i]==0):
			last_zero=i
	if(first_one>last_zero):
		print(0)
		break
	else:
		ans=min(l.count(0),l.count(1))
		oo=0
		ans3=0
		for i in range(len(l)):
			if(l[i]==1):
				oo+=1
			else:
				if(oo>0):
					oo-=1
					ans3+=1
		ans=min(ans,ans3)
		print(ans)