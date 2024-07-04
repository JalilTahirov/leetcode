nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6] 
n = 3
p2 = 0
for p1 in range(m + n -1):
    if nums1[p1] > nums2[p2]:
        prev = nums1[p1]
        for i in range(p1+1, len(nums1)):
            temp =  nums1[i]
            nums1[i] = prev 
            prev = temp
    nums1[p1] =  nums2[p2]
print(nums1)



