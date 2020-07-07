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

def f(s):
	s=[int(i)-1 for i in s]
	n=len(s)
	visited=[0,0,0]
	start=0
	start_index=0
	min_len=2**32
	count=0
	curr_count=[0,0,0]
	for i in range(n):
		curr_count[s[i]]+=1
		if(curr_count[s[i]]==1):
			count+=1
		if(count==3):
			while (curr_count[s[start]]>1):
				if (curr_count[s[start]] > 1): 
					curr_count[s[start]]-=1 
				start+=1 
			len_window = i - start + 1 
			if(min_len > len_window): 
				min_len = len_window 
				start_index = start 
	s=s[start_index:start_index+min_len]
	return len(s)


for _ in range(int(input())):
	s=list(input()[:-1])
	if('1' in s and '2' in s and '3' in s):
		print(f(s))
	else:
		print(0)