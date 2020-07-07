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

closest=-1
def bs(arr, l, r, x):
	if(l <= r): 
		mid =l + (r-l)//2
		if arr[mid]==x: 
			return mid
		elif arr[mid] < x:
			return bs(arr,mid+1,r,x)
		else:
			return bs(arr,l,mid-1,x) 
	return l

input=stdin.readline

def list_input():
	return list(map(int, input().split()))

def sep_input():
	return map(int, input().split())

#_______________________________________________________________________________________________________________________________________

l=[2]
for i in range(1,26000):
	l.append(l[-1]+3*(i)+2)
for _ in range(int(input())):
	n=int(input())
	ans=0
	while(True):
		#print(n)
		if(n<=1):
			break
		else:
			ans+=1
			temp=bs(l,0,len(l)-1,n)
			if(l[temp]==n):
				n=n-l[temp]
			elif(l[temp]<n):
				f=l[temp]
				for i in range(temp,len(l)):
					if(l[i]>n):
						break
					else:
						f=l[i]
				n=n-f
			else:
				f=l[temp]
				for i in range(temp,-1,-1):
					if(l[i]<n):
						f=l[i]
						break
				n=n-f
	print(ans)