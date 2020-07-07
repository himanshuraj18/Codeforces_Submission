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

s=input()
n=len(s)
l=[]
for i in range(n-1):
	if(s[i]=='v' and s[i+1]=='v'):
		l.append(1)
	else:
		l.append(0)
l.append(0)
c=0
pref=[]
for i in range(n):
	c+=l[i]
	pref.append(c)
ans=0
for i in range(n):
	if(s[i]=='o'):
		t1=pref[i]
		t2=pref[-1]-pref[i]
		ans+=(t1)*(t2)
# print(l)
# print(pref)
print(ans)