nums=list(map(int,input().split()))
si=0
li=len(nums)-1
while si<=li:
    mid=(si+li)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]>=nums[si]:
        if target>=nums[si] and target<=nums[mid]:
           li=mid-1
        else:
           si=mid+1
    else:
        if target>=nums[mid] and target<=nums[li]:
            si=mid+1
        else:
            li=mid-1
return -1
               
        
        