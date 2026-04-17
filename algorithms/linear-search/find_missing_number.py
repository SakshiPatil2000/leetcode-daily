"""
  Find the missing number in a list containing numbers from 1 to n.
  
  Approach :
  Calculate the expected sum of numbers from 1 to n using formula n*(n+1)/2.
  Calculate the actual sum of elements present in the array.
  The difference between expected sum and actual sum gives the missing number.  
  
  Time Complexity: O(n)
  Space Complexity: O(1) -> no extra space used
    
"""



def findMissingNumber(arr):
    n =len(arr) + 1
    expectedSum = n*(n+1) // 2
    actual_sum=sum(arr)
    
    missing_number = expectedSum - actual_sum
    
    return missing_number

arr =[1,2,4,5,6]
print(findMissingNumber(arr))
