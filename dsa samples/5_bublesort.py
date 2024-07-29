arr = [2,3,4,5,3,9,2,10]
print(arr)
for i in range(1, len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1] and j+1 < len(arr):
            arr[j],arr[j+1] = arr[j+1], arr[j]

print(arr)


