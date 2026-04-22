"""
  Find sub array with given sum return start and end index.
  
  Approach :
  Use Sliding Window Solution
  
  Time Complexity : O(n)
  Spcae Complexity : O(1)
     
"""

def findSubarrayWithGivemSum(arr,total):
    start = 0
    currentSum = 0
    
    for end in range(len(arr)):
        currentSum += arr[end]
        
        #shrink window if currentsum is > total
        while currentSum > total:
            currentSum -= arr[start]
            start += 1
            
        #check is currentsum equals to total
        
        if currentSum == total:
            return start,end
        
    return -1


arr = [1,4,20,3,10,5]
total =33
print(findSubarrayWithGivemSum(arr,33))
                
        
    
    