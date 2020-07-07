import sys
# from collections import Counter
# from math import ceil,log

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

fast_reader=sys.stdin.readline

def input():
	return fast_reader().strip()

def list_input():
	return list(map(int, input().split()))

def sep_input():
	return map(int, input().split())

#_______________________________________________________________________________________________________________________________________

for _ in range(int(input())):
	n,m=sep_input()
	l=[]
	for i in range(n):
		l.append(list_input())
	c1=[0 for i in range(n)]
	c2=[0 for i in range(m)]
	for i in range(n):
		for j in range(m):
			if(l[i][j]==1):
				c1[i]+=1
				c2[j]+=1
	c1=c1.count(0)
	c2=c2.count(0)
	if(min(c1,c2)%2==0):
		print('Vivek')
	else:
		print('Ashish')