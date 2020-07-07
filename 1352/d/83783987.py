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
	n=int(input())
	l=list_input()
	prev=-1
	a=0
	b=0
	i=0
	j=n-1
	sa=0
	sb=0
	moves=0
	while(True):
		f1=False
		f2=False
		temp=0
		for pp in range(i,j+1):
			temp+=l[pp]
			if(temp>prev):
				i=pp+1
				f1=True
				prev=temp
				break
		if(f1):
			sa+=prev
			moves+=1
		else:
			sa+=temp
			moves+=1
			break
		if(i>j):
			break
		temp=0
		for pp in range(j,i-1,-1):
			temp+=l[pp]
			#print(temp)
			if(temp>prev):
				f2=True
				j=pp-1
				prev=temp
				break
		if(f2):
			sb+=prev
			moves+=1
		else:
			sb+=temp
			moves+=1
			break
		if(i>j):
			break
	print(moves,sa,sb)