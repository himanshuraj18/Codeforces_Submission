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
	r1,c1=map(int, input().split())
	r2,c2=map(int, input().split())
	r1-=1
	r2-=1
	c1-=1
	c2-=1
	l=[]
	for i in range(n):
		pp=list(input())
		pp=[int(j) for j in pp]
		l.append(pp[:])
	l1=[]
	q1=deque([(r1,c1)])
	visited=[[0 for i in range(n)] for j in range(n)]
	while(len(q1)>0):
		x,y=q1.popleft()
		if(visited[x][y]==1):
			continue
		else:
			visited[x][y]=1
			l1.append((x,y))
			if(x-1>=0 and l[x-1][y]==0):
				q1.append((x-1,y))
			if(y-1>=0 and l[x][y-1]==0):
				q1.append((x,y-1))
			if(x+1<n and l[x+1][y]==0):
				q1.append((x+1,y))
			if(y+1<n and l[x][y+1]==0):
				q1.append((x,y+1))
	#print(l1)
	if((r2,c2) in l1):
		print(0)
		continue
	l2=[]
	q2=deque([(r2,c2)])
	visited=[[0 for i in range(n)] for j in range(n)]
	while(len(q2)>0):
		x,y=q2.popleft()
		if(visited[x][y]==1):
			continue
		else:
			visited[x][y]=1
			l2.append((x,y))
			if(x-1>=0 and l[x-1][y]==0):
				q2.append((x-1,y))
			if(y-1>=0 and l[x][y-1]==0):
				q2.append((x,y-1))
			if(x+1<n and l[x+1][y]==0):
				q2.append((x+1,y))
			if(y+1<n and l[x][y+1]==0):
				q2.append((x,y+1))
	#print(l2)
	ans=2**40
	for i in range(len(l1)):
		for j in range(len(l2)):
			rs,cs=l1[i]
			rs+=1
			cs+=1
			rt,ct=l2[j]
			rt+=1
			ct+=1
			ans=min(ans, (rs-rt)**2 + (cs-ct)**2)
	print(ans)