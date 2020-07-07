n=int(input())
arr=list(map(int, input().split()))
a=[]
for i in range(n):
	for j in range(n):
		if(i!=j):
			a.append(arr[i]+arr[j])
			#print(arr[i],"+",arr[j],"=",arr[i]+arr[j])
d={}
for i in range(len(a)):
	d[a[i]]=0
for i in range(len(a)):
	d[a[i]]+=1
l=list(d.values())
k=list(d.keys())
# print(l,sum(l))
# print(k)
# print(d)
print(max(l)//2)