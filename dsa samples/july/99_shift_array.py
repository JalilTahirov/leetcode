
nums1 = [2,0]
nums2 = [1]
m,n = 1,1

r_p = m + n - 1
p1 = m - 1
p2 = n - 1

while p2 >= 0:
  if p1 >= 0 and nums1[p1] > nums2[p2]:
    print(p1)
    nums1[r_p] = nums1[p1]
    p1 -= 1
  else:
    nums1[r_p] = nums2[p2]
    p2 -= 1
  r_p -= 1
  print(nums1[p1], nums2[p2])

print(nums1)







'''
arr = [1,0,3,4,5,6]
j = 0
while j < len(arr):
  if arr[j] == 0:    
    for i in range(len(arr) -1, j , -1):
      arr[i] = arr[i-1]
    j +=1
  j+=1


print(arr)
'''

  