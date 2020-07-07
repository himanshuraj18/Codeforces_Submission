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

for _ in range(int(input())):
	n,k=map(int, input().split())
	a=list(map(int, input().split()))
	w=list(map(int, input().split()))
	a.sort(reverse=True)
	w.sort()
	ones=w.count(1)
	ans=2*(sum(a[:ones]))
	a=a[ones:]
	w=w[ones:]
	w.sort(reverse=True)
	a.sort()
	st=0
	en=len(a)-1
	for i in range(len(w)):
		ans+=a[en]+a[st]
		en-=1
		st+=w[i]-1
	print(ans)