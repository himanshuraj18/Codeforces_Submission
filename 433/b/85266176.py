import sys
# from collections import deque
# from collections import Counter
# from math import sqrt
# from math import log
# from math import ceil

# alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# mod=10**9+7
# mod=998244353

fast_reader=sys.stdin.readline
fast_writer=sys.stdout.write

def input():
	return fast_reader().strip()

def print(*argv):
	fast_writer(' '.join((str(i)) for i in argv))
	fast_writer('\n')

#____________________________________________________________________________________________________________________________________

n=int(input())
v=list(map(int, input().split()))
u=sorted(v)
prefv=[]
prefu=[]
c1=0
c2=0
for i in range(n):
	c1+=v[i]
	c2+=u[i]
	prefv.append(c1)
	prefu.append(c2)
q=int(input())
for _ in range(q):
	t,l,r=map(int, input().split())
	l=l-1
	r=r-1
	if(t==1):
		if(l==0):
			print(prefv[r])
		else:
			print(prefv[r]-prefv[l-1])
	else:
		if(l==0):
			print(prefu[r])
		else:
			print(prefu[r]-prefu[l-1])