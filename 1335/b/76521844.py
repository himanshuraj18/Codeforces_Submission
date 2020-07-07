l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for _ in range(int(input())):
	n,a,b=map(int, input().split())
	if(b==1):
		s='a'*n
	else:
		ss=''
		for i in range(b):
			ss+=l[i]
		s=ss*(n//b)+ss[:n%b]
	print(s)