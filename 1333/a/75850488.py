for _ in range(int(input())):
    n,m=map(int, input().split())
    l=['B'*m for i in range(n)]
    l[0]='W'+l[0][1:]
    for i in range(n):
    	print(l[i])