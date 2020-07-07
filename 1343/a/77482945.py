l=[]
for i in range(2,40):
	l.append(2**(i)-1)
for _ in range(int(input())):
	n=int(input())
	for i in range(len(l)):
		if(n%l[i]==0):
			print(n//l[i])
			break