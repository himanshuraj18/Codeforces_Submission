for _ in range(int(input())):
	n=int(input())
	l=list(map(int, input().split()))
	maxi=max(l)
	mini=min(l)
	if(maxi<0 or mini>0):
		print(maxi)
	else:
		if(l[0]>0):
			f=-1
		else:
			f=1
		s=0
		c=0
		i=0
		l1=[]
		while(i<n):
			if(l[i]>0 and f==-1):
				j=i
				mm=l[i]
				while(j<n):
					if(l[j]<0):
						j-=1
						break
					else:
						if(l[j]>mm):
							mm=l[j]
					j+=1
				s+=mm
				i=j
				f=1
				c+=1
			elif(l[i]<0 and f==1):
				j=i
				mm=l[i]
				while(j<n):
					if(l[j]>0):
						j-=1
						break
					else:
						if(l[j]>mm):
							mm=l[j]
					j+=1
				s+=mm
				i=j
				f=-1
				c+=1
			l1.append(mm)
			i+=1
		#print(l1)
		print(s)