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
	n=int(input())
	d={}
	p=[]
	for i in range(n):
		old,new=input().split()
		d[old]=new
		p.append(old)
	visited=set()
	ans=0
	lans=[]
	for i in range(len(p)):
		if(p[i] in visited):
			continue
		ans+=1
		old=p[i]
		q=deque()
		q.append(p[i])
		new=""
		while(len(q)!=0):
			t=q.popleft()
			if(t in visited):
				continue
			elif(t not in d):
				visited.add(t)
				break
			else:
				visited.add(t)
				new=d[t]
				q.append(d[t])
		lans.append([old,new])
	print(ans)
	for i in range(len(lans)):
		print(*lans[i])