"""
  Find element with maximum frequency.
  
  Approach :
  For every element, count its frequency using a second loop.
  Keep track of the element with the highest frequency.  
  Return the element with maximum count. 
  
  Time Complexity: O(n^2)
  Space Complexity: O(1)
  
"""


def findMaxFreqElement(arr):
    n = len(arr)
    max_count = 0
    max_element = -1
    
    for i in range(n):
        count = 0
        
        for j in range(n):
            if arr[i] == arr[j]:
                count +=1
        
        #update max element
        
        if count > max_count:
            max_count = count
            max_element = arr[i]
            
    return max_element

arr =[1,4,5,6,7,8,9,3,2,3,4,5,2,2,3,3,45,7,4,5,6,6,6]
print(findMaxFreqElement(arr))
