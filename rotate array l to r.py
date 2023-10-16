''' left to right'''

'''l=list(map(int,input().split()))
k=int(input())
for i in range(k):
    l.append(l.pop(0))
print(l)'''

l=list(map(int,input().split()))
k=int(input())
a=k
l[:]=l[a:]+l[:a]
print(l)