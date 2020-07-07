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
	n,x,m=sep_input()
	l=[]
	r=[]
	a,b=x,x
	for i in range(m):
		t1,t2=sep_input()
		l.append(t1)
		r.append(t2)
		if(t1<=a and t2>=b):
			a=t1
			b=t2
		elif(t1<=a<=t2<=b):
			a=t1
		elif(a<=t1<=b<=t2):
			b=t2
	print(b-a+1)