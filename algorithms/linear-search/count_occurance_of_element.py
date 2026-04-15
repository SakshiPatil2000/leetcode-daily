def countOccurance(arr,target):
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            count +=1
    
    return f"{target} occures {count} times"

arr =[12,23,45,67,89,54,23,45,67,23,78,23]
target=23
print(countOccurance(arr,target))