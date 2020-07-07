def f(n):
	n=str(n)
	c=0
	for i in range(len(n)):
		c+=int(n[i])
	return c
n=int(input())
while True:
	if(f(n)%4==0):
		print(n)
		break
	else:
		n+=1