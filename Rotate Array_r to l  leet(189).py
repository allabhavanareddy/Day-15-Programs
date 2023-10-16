''' right to left
 Given an integer array nums, rotate the array
to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]'''

l=list(map(int,input().split()))
k=int(input())
for i in range(k):
    l.insert(0,l.pop())
print(l)


#using temp variable

l=list(map(int,input().split()))
k=int(input())
n=len(l)
for i in range(k):
    temp=l[-1] #l[-1] is last elemnt
    for j in range(n-1,0,-1):#moves from last ele to first decr by 1
        l[j]=l[j-1]#stores last befor ele in last
    l[0]=temp#now 1st ele replace by temp
print(l)



#using slicing
l=list(map(int,input().split()))
k=int(input())
a=len(l)-k
l[:]=l[a:]+l[:a]
print(l)