n,a,x,b,y=map(int, input().split())
l=[a]
l1=[b]
while a!=x:
	a+=1
	if(a==n+1):
		a=1
	l.append(a)
while b!=y:
	b-=1
	if(b==0):
		b=n
	l1.append(b)
#print(l,l1)
f="NO"
for i in range(min(len(l1),len(l))):
	if(l1[i]==l[i]):
		f="YES"
print(f)