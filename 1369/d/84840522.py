import sys
# from collections import deque
# from collections import Counter
# from math import sqrt
# from math import log
# from math import ceil

# alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mod=10**9+7
# mod=998244353

fast_reader=sys.stdin.readline
fast_writer=sys.stdout.write

def input():
	return fast_reader().strip()

def print(*argv):
	fast_writer(' '.join((str(i)) for i in argv))
	fast_writer('\n')

#____________________________________________________________________________________________________________________________________


dp=[0 for i in range(2*(10**6)+5)]
for i in range(3,len(dp)):
	dp[i]=(dp[i-1]+((2*dp[i-2])%mod))%mod
	if(i%3==0):
		dp[i]=(dp[i]+4)%mod
for _ in range(int(input())):
	n=int(input())
	print(dp[n])