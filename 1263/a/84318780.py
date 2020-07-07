import sys
# from collections import deque
# from collections import Counter
# from math import sqrt
from math import log
from math import ceil

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
	l=list(map(int, input().split()))
	l.sort()
	diff=l[2]-l[1]
	if(diff>=l[0]):
		print(l[0]+l[1])
	else:
		l[2]-=diff
		l[0]-=diff
		l[2]=l[2]-(l[0]//2)
		l[1]=l[2]
		print(l[1]+diff+2*(l[0]//2))