import sys
from collections import deque
# from math import sqrt

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
# 	s=set()
# 	for i in range(len(prime)):
# 		if(prime[i]):
# 		s.add(i)
# 	return s 

# alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# mod=10**9+7

fast_reader=sys.stdin.readline
fast_writer=sys.stdout.write

def input():
	return fast_reader().strip()

def print(*argv):
	fast_writer(' '.join(str(i) for i in argv)+'\n')

def list_input():
	return list(map(int, input().split()))

def sep_input():
	return map(int, input().split())

#_______________________________________________________________________________________________________________________________________

for _ in range(int(input())):
	n=int(input())
	l=[]
	visited=[[False for i in range(n)] for j in range(n)]
	for i in range(n):
		temp=[int(i) for i in input()]
		l.append(temp[:])
	q=deque()
	for i in range(n):
		if(l[i][n-1]==1):
			q.append((i,n-1))
		if(l[n-1][i]==1):
			q.append((n-1,i))
	while(len(q)!=0):
		a=q.popleft()
		r=a[0]
		c=a[1]
		if(visited[r][c]):
			continue
		else:
			visited[r][c]=True
			if(r-1>=0):
				if(l[r-1][c]==1):
					q.append((r-1,c))
			if(c-1>=0):
				if(l[r][c-1]==1):
					q.append((r,c-1))
	f=True
	for i in range(n):
		for j in range(n):
			if(l[i][j]==1 and visited[i][j]==False):
				f=False
				break
	if(f):
		print('YES')
	else:
		print('NO')