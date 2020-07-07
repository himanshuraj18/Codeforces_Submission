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
	# if(n<=1000):
	# 	for i in range(1,n+1):
	# 		c=0
	# 		cand=n
	# 		m=i
	# 		while(cand>0):
	# 			temp=min(m,cand)
	# 			cand-=temp
	# 			c+=temp
	# 			cand-=cand//10
	# 		if(c*2>=n):
	# 			print(m)
	# 			break	
	# 	continue
	l=1
	r=n
	ans=2**100
	while(l<=r):
		m=l+(r-l)//2
		c=0
		cand=n
		while(cand>0):
			temp=min(m,cand)
			cand-=temp
			c+=temp
			cand-=cand//10
		if(c*2>=n):
			ans=min(ans,m)
			r=m-1
		else:
			l=m+1
	print(ans)