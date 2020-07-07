from math import ceil
for _ in range(int(input())):
	n=int(input())
	l=list(map(int, input().split()))
	s=sum(l)
	print(ceil(s/n))