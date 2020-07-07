n=int(input())
s=input()
# l=[]
# for i in range(n):
# 	for j in range(n):
# 		if(i<=j):
# 			l.append(int(s[i:j+1]))
# c=0
# for i in l:
# 	if(i%2==0):
# 		c+=1
# print(c)
c=0
for i in range(n):
	if(int(s[i])%2==0):
		c+=i+1
print(c)