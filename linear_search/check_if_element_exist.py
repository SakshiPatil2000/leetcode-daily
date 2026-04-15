def checkElementExist(arr,target):
    for num in arr:
        if num == target:
            return True
        
    return False

arr =[10,20,23,15,27,38,49,34]
target=34
print(checkElementExist(arr,target))