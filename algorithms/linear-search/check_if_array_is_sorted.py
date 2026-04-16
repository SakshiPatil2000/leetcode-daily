"""
    Check if an array is sorted in ascending order.
    
    Approach:    
    We only compare adjacent elements, because in a sorted array every element must be ≤ next element.
    
    Time Complexity : O(n)
    Space Complexity : O(1) no extra space used
    """


def checkArraySorted(arr):
    for i in range(len(arr) -1):
            if arr[i] > arr[i+1]:
                return False
            
    return True

arr =[10,20,30,45,34]
print(checkArraySorted(arr))
