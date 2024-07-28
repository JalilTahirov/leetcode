arr = [2,9,1,1,1,2,4,6,]
print(arr)

for i in range(1, len(arr)):
    j = i-1
    while j >= 0 and arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        j -= 1

print(arr)
