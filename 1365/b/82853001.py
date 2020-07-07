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


def bubbleSort(arr,b): 
	n = len(arr) 
	# Traverse through all array elements 
	for i in range(n): 
		# Last i elements are already in place 
		for j in range(0, n-i-1): 
			# traverse the array from 0 to n-i-1 
			# Swap if the element found is greater 
			# than the next element 
			if arr[j] > arr[j+1] and b[j]!=b[j+1] : 
				arr[j], arr[j+1] = arr[j+1], arr[j]
				b[j] , b[j+1] = b[j+1] , b[j]
	return arr 
	
for _ in range(int(input())):
	n=int(input())
	a=list_input()
	b=list_input()
	if(a==sorted(a)):
		print('YES')
		continue
	if(len(set(b))==1):
		print('NO')
		continue
	z=[]
	o=[]
	for i in range(n):
		if(b[i]==0):
			z.append(a[i])
		else:
			o.append(a[i])
	z.sort()
	o.sort()
	x=0
	y=0
	for i in range(n):
		if(b[i]==0):
			a[i]=z[x]
			x+=1
		else:
			a[i]=o[y]
			y+=1
	l=bubbleSort(a,b)
	if(l==sorted(l)):
		print('YES')
	else:
		print('NO')