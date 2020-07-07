n=int(input())
l=[]
d={}
d1={}
d2={}
c=0
for i in range(97,123):
    d[chr(i)]=0
    d2[chr(i)]=0
    d1[chr(i)]=0
for i in range(n):
    s=input()
    l.append(s[0])
    d[s[0]]+=1
for i in range(97,123):
    d1[chr(i)]+=d[chr(i)]//2
    d2[chr(i)]+=d[chr(i)]-d[chr(i)]//2
for i in range(97,123):
    x=d1[chr(i)]
    y=d2[chr(i)]
    c+=x*(x-1)/2
    c+=y*(y-1)/2
print(int(c))