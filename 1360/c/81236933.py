from sys import stdin
# from collections import Counter
from math import ceil,sqrt

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
	n=int(input())
	l=list_input()
	l.sort()
	even=0
	odd=0
	for i in range(n):
		if(l[i]%2==1):
			odd+=1
		else:
			even+=1
	if(even%2==0 and odd%2==0):
		print('YES')
	else:
		f=False
		for i in range(1,n):
			if(l[i]-l[i-1]==1):
				f=True
				break
		if(f):
			print('YES')
		else:
			print('NO')