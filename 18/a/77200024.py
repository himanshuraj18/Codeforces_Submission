def f(x1,y1,x2,y2,x3,y3):
	d1=(x1-x2)**2+(y1-y2)**2
	d2=(x2-x3)**2+(y2-y3)**2
	d3=(x3-x1)**2+(y3-y1)**2
	l=[d1,d2,d3]
	l.sort()
	if(l[0]+l[1]!=l[2] or l[1]==l[2]):
		return False
	else:
		return True
x1,y1,x2,y2,x3,y3=map(int, input().split())
if(f(x1,y1,x2,y2,x3,y3)):
	print('RIGHT')
elif(f(x1-1,y1,x2,y2,x3,y3) or f(x1,y1-1,x2,y2,x3,y3) or f(x1,y1,x2-1,y2,x3,y3) or f(x1,y1,x2,y2-1,x3,y3) or f(x1,y1,x2,y2,x3-1,y3) or f(x1,y1,x2,y2,x3,y3-1)):
	print('ALMOST')
elif(f(x1+1,y1,x2,y2,x3,y3) or f(x1,y1+1,x2,y2,x3,y3) or f(x1,y1,x2+1,y2,x3,y3) or f(x1,y1,x2,y2+1,x3,y3) or f(x1,y1,x2,y2,x3+1,y3) or f(x1,y1,x2,y2,x3,y3+1)):
	print('ALMOST')
else:
	print('NEITHER')