for _ in range(int(input())):
	n=int(input())
	if(n%4!=0):
		print('NO')
		continue
	else:
		print('YES')
		ev=[]
		od=[]
		for i in range(1,10000000,5):
			if(len(ev)+len(od)>=n):
				break
			if(i%2==1):
				ev.append(i+1)
				ev.append(i+3)
				od.append(i)
				od.append(i+4)
			else:
				od.append(i+1)
				od.append(i+3)
				ev.append(i)
				ev.append(i+4)
		l=ev+od
		print(*l)