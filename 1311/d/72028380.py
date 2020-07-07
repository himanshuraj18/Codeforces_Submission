for _ in range(int(input())):
    a,b,c=map(int, input().split())
    ans=100000000000
    aa=0
    bb=0
    cc=0
    for i in range(1,11000):
        for j in range(i,11000,i):
            for k in range(j,11000,j):
                if(j%i==0 and k%j==0):
                    m=abs(a-i)+abs(b-j)+abs(c-k)
                    #print(i,j,k,m)
                    if(m<ans):
                        #print(ans)
                        aa=i
                        bb=j
                        cc=k
                        ans=m
                        if(ans==0):
                            break
            if(ans==0):
                break
        if(ans==0):
            break    
    print(ans)
    print(aa,bb,cc)