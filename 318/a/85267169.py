n,k=map(int, input().split())
if(k==(n+1)//2):
    if(n%2==0):
        print(n-1)
    else:
        print(n)
elif(k>(n+1)//2):
    print((k-(n+1)//2)*2)
else:
    print(k%((n+1)//2)*2-1)