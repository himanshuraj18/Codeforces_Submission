import sys
# from collections import deque
# from collections import Counter
# from math import sqrt
# from math import log
# from math import ceil
# from bisect import bisect_left, bisect_right

alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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

def k(r1,c1,r2,c2):
	diffr=abs(r1-r2)
	diffc=abs(c1-c2)
	moves=max(diffc,diffr)
	return moves

def r(r1,c1,r2,c2):
	if(r1==r2 and c1==c2):
		return 0
	elif(r1==r2 or c1==c2):
		return 1
	else:
		return 2

def b(r1,c1,r2,c2):
	if((r1+c1)%2!=(r2+c2)%2):
		return 0
	elif(abs(r1-r2)==abs(c1-c2)):
		return 1
	else:
		return 2

r1,c1,r2,c2=map(int, input().split())
print(r(r1,c1,r2,c2),b(r1,c1,r2,c2),k(r1,c1,r2,c2))