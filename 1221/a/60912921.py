for _ in range(int(input())):
    n=int(input())
    li=list(map(int, input().split()))
    l=[]
    f=0
    s=0
    for i in range(n):
        if(li[i]==2048):
            print("YES")
            f=1
            break
        elif(li[i]<2048):
            s+=li[i]
        if(s>=2048):
            f=1
            print("YES")
            break
    if(f==1):
        continue
    else:
        print("NO")