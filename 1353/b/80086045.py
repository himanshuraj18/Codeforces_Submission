from sys import stdin
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

input=stdin.readline

def list_input():
	return list(map(int, input().split()))

def sep_input():
	return map(int, input().split())

#_______________________________________________________________________________________________________________________________________

for _ in range(int(input())):
	n,k=sep_input()
	a=list_input()
	b=list_input()
	if(k==0):
		print(sum(a))
	else:
		a.sort()
		b.sort(reverse=True)
		i=0
		j=0
		while(i<n and j<n and k>0):
			if(a[i]<b[j]):
				temp=a[i]
				a[i]=b[i]
				b[i]=temp
				i+=1
				j+=1
				k-=1
			else:
				break
		print(sum(a))