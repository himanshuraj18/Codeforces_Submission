for _ in range(int(input())):
	n = int(input())
	l=list(map(int, input().split()))
	l.sort()
	midi=False
	if(n%2==1):
		midi=True
		mid=l[n//2]
		l=l[:n//2]+l[(n//2)+1:]
		n=n-1
	a=[]
	for i in range(n//2):
		a.append(l[i])
		a.append(l[n-i-1])
	if(midi):
		f=False
		if(abs(a[0]-mid)>=abs(a[1]-a[0])):
			a=[mid]+a
		elif(abs(a[-1]-a[-2])>=abs(a[-1]-mid)):
			a=a+[mid]
		else:	
			for i in range(n-1):
				if(abs(a[i]-mid)>=abs(a[i+1]-mid)):
					a=a[:i+1]+[mid]+a[i+1:]
					f=True
					break
	a=a[::-1]
	print(*a)
