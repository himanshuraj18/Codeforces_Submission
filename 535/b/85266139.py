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
 
s=list(input())
c=1
for i in range(len(s)):
	c*=2
	if(s[i]=='7'):
		c+=1
print(c-1)