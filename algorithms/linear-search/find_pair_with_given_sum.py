"""
   Find indices of a pair of consecutive elements whose sum equals the given number
   
   Approach:
   Traverse the array and for each index, calculate the sum of the current
   element and the next element (arr[i] + arr[i+1]).
   If the sum matches the target number, return their indices.
   If no such pair is found, return -1.
   
   Time Complexity: O(n) 
   Space Complexity: O(1) → no extra space used
"""


def findPairWithGivenSum(arr,number):
    for i in range(len(arr)):
       total=0
       total= arr[i] + arr[i+1]
       if total == number:
           return i,i+1
       
    return -1


arr =[1,6,4,5,7]
number =9
print(findPairWithGivenSum(arr,number))
       