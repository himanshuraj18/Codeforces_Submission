from sys import stdin
# from collections import Counter
from math import ceil

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
# 	return prime 

# alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# mod=10**9+7

input=stdin.readline

def list_input():
	return list(map(int, input().split()))

def sep_input():
	return map(int, input().split())

#_______________________________________________________________________________________________________________________________________

for _ in range(int(input())):
	n,m,x,y=sep_input()
	l=[]
	for i in range(n):
		l.append([i for i in input()[:-1]])
	i=0
	c=0
	while(i<n):
		j=0
		while(j<m):
			if(l[i][j]=='.'):
				if(j!=m-1 and l[i][j+1]=='.'):
					c+=min(2*x,y)
					j+=2
					continue
				else:
					c+=x
					j+=1
					continue
			j+=1
		i+=1
	print(c)