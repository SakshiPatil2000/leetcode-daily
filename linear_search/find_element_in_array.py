def findElement(arr,target):
    for num in arr:
        if num == target:
            return True
        
    return False 

arr = [10,20,30,24,19,13,45]
target =45

print(findElement(arr,target))