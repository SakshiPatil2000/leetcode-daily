def findElement(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1 

arr = [10,20,30,24,19,13,45]
target =45

print(findElement(arr,target))