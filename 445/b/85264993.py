import sys
from collections import deque
# from collections import Counter
# from math import sqrt
# from math import log
# from math import ceil
# from bisect import bisect_left, bisect_right

# alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mod=10**9+7
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
	n,m=map(int, input().split())
	d={}
	for i in range(n):
		d[i]=[]
	for i in range(m):
		x,y=map(int, input().split())
		x=x-1
		y=y-1
		d[x].append(y)
		d[y].append(x)
	visited=set()
	ans=1
	#print(d)
	for i in range(n):
		if(i in visited):
			continue
		#print(i,visited)
		c=0
		q=deque()
		q.append(i)
		while(len(q)!=0):
			t=q.popleft()
			if(t in visited):
				continue
			else:
				visited.add(t)
				c+=1
				for j in d[t]:
					q.append(j)
		#print(i,visited)
		ans*=max(1,2**(c-1))
	print(ans)