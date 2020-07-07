import sys
# from collections import deque
# from collections import Counter
# from math import sqrt
# from math import log
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

# def print(*argv):
# 	fast_writer(' '.join((str(i)) for i in argv))
# 	fast_writer('\n')

def list_input():
	return list(map(int, input().split()))

def sep_input():
	return map(int, input().split())

#_______________________________________________________________________________________________________________________________________

for _ in range(int(input())):
	n,k=sep_input()
	s=list(input())
	l=[int(i) for i in s]
	st=[]
	for i in range(n):
		if(l[i]==1):
			st.append(i)
	if(n<=k):
		if(len(st)>0):
			print(0)
		else:
			print(1)
	elif(len(st)==0):
		print(ceil(n/(k+1)))
	else:
		c=0
		for i in range(len(st)-1):
			temp=st[i+1]-st[i]-1
			#print(temp)
			temp-=2*k
			#print(temp)
			if(temp>0):
				c+=ceil(temp/(k+1))
		c+=max(0,ceil((st[0]-k)/(k+1)))
		c+=max(0,ceil((n-st[-1]-1-k)/(k+1)))
		print(c)