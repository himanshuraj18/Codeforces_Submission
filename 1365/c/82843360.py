import sys
from collections import Counter
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

n=int(input())
a=list_input()
b=list_input()
da={}
db={}
for i in range(n):
	da[a[i]]=i
	db[b[i]]=i
r={}
for i in range(1,n+1):
	if(da[i]-db[i]>=0):
		r[i]=da[i]-db[i]
	else:
		r[i]=n+(da[i]-db[i])
#print(r)
p1=list(r.values())
d1=Counter(p1)
print(max(list(d1.values())))