"""
    Find last occurance index of target in arrayy.
    
    Approaches:
    1. Reverse linear search
    
    Time Complexity : O(n)
    Space Complexity : O(n)
"""



def lastOccuranceindex(arr,target):
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == target:
            return i
        
    return -1

arr = [12,34,26,12,67,34,78,12,34]
target =12
print(lastOccuranceindex(arr, target))