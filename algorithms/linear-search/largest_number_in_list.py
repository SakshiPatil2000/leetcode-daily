"""
 Find the largest number in an array using Linear Search.
 
 Approach:
 1.Iterate through the array and keep updating the largest number so far 
 
 Time Complexity : O(n)
 Space Complexity : O(n)
"""


def largestNumber(arr):
    largest = arr[0]
    
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            
    return largest

arr =[12,24,35,67,89,23,56,478,56,89,99]
print(largestNumber(arr))