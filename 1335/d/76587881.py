from collections import Counter
for _ in range(int(input())):
	l=[]
	for i in range(9):
		l.append(input())
	p=[(0,0),(1,3),(2,6),(3,1),(4,4),(5,7),(6,2),(7,5),(8,8)]
	for x in range(9):
		i=p[x][0]
		j=p[x][1]
		if(l[i][j]!='9'):
			l[i]=l[i][:j]+'9'+l[i][j+1:]
			#print(l[i][:j]+'9'+l[i][j+1:])
		else:
			l[i]=l[i][:j]+'1'+l[i][j+1:]
			#print(l[i]=l[i][:j]+'1'+l[i][j+1:])
		#print()
		#print(i,j)
		print(l[i])