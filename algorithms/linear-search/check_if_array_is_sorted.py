def checkArraySorted(arr):
    for i in range(len(arr) -1):
            if arr[i] > arr[i+1]:
                return False
            
    return True

arr =[10,20,30,45,34]
print(checkArraySorted(arr))
