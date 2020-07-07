from sys import stdin
# from collections import Counter
from math import log

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

l=set()
for i in range(200):
	l.add(2**i)

for _ in range(int(input())):
	a,b=sep_input()
	if(a>=b and a%b==0):
		c=a//b
		if(c in l):
			need=int(log(c,2))
			ans1=need//3
			ans2=(need-3*ans1)//2
			ans3=(need-(3*ans1)-(2*ans2))
			print(ans1+ans2+ans3)
		else:
			print(-1)
	elif(b>=a and b%a==0):
		c=b//a
		if(c in l):
			need=int(log(c,2))
			ans1=need//3
			ans2=(need-3*ans1)//2
			ans3=(need-(3*ans1)-(2*ans2))
			print(ans1+ans2+ans3)
		else:
			print(-1)
	else:
		print(-1)