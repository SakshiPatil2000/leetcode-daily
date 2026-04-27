"""
  Find element that appears once.
  
  Approach:
  Use Bit Manipulation(XOR)
  
  Time Complexity : O(n)
  Space Complexity : O(1)  

"""

def findElementThatAppearsOnce(arr):
    result = 0
    
    for num in arr:
        
         result ^= num
         
    return result

arr = [2,3,5,4,5,3,4]
print(findElementThatAppearsOnce(arr))