from sys import stdin
# from collections import Counter
# from math import ceil, log

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
	n,x=sep_input()
	l=list_input()
	if(x==n):
		if(sum(l)%2==1):
			print('YES')
		else:
			print('NO')
		continue
	o=[]
	e=[]
	for i in range(n):
		if(l[i]%2==1):
			o.append(l[i])
		else:
			e.append(l[i])
	if(len(o)==0):
		print('NO')
	elif(len(o)==n):
		if(x%2==0):
			print('NO')
		else:
			print('YES')
	else:
		k=x
		s=0
		for i in range(len(o)):
			if(k==0 or (s%2==1 and len(e)>=k and k>0)):
				break
			else:
				k-=1
				s+=o[i]
		if(k==0 and s%2==1):
			print('YES')
		elif(k==0 and s%2==0):
			print('NO')
		elif(s%2==1 and len(e)>=k and k>0):
			print('YES')
		else:
			for i in range(len(e)):
				if(k==0):
					break
				else:
					k-=1
					s+=e[i]
			if(s%2==1):
				print('YES')
			else:
				print('NO')
