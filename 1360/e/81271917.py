from sys import stdin
from collections import deque

# def gcd(a, b):
# 	if(a==0):
# 		return b 
# 	return gcd(b%a,a)

def sieve(n): 
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

# alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# mod=10**9+7

input=stdin.readline

def list_input():
	return list(map(int, input().split()))

def sep_input():
	return map(int, input().split())

#_______________________________________________________________________________________________________________________________________

def factors(n,k):
	l=[]
	m=1
	for i in range(1,min(k,ceil(sqrt(n)))+1):
		if(n%i==0):
			if(n//i==i):
				if(i>m and i<=k):
					m=i
			else:
				if(i>m and i<=k):
					m=i
				if(n//i>m and n//i<=k):
					m=n//i
	return m

for _ in range(int(input())):
	n=int(input())
	l=[]
	visited=[[False for i in range(n)] for j in range(n)]
	for i in range(n):
		temp=[int(i) for i in input()[:-1]]
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