"""
  Find the smallest missing positive integer from an unsorted array.
  
  Approach:
  Store all positive numbers in a set.
  Start checking from 1.
  First number not present → answer.
  
  Time Complexity: O(n)
  Space Complexity: O(n)
    """

def findSmallestMissingPositiveNumber(arr):
    positives=set()
    for num in arr:
        if num > 0:
            positives.add(num)
            
    i=1
    while True:
        if i not in positives:
            return i
        i += 1

arr =[3,4,-1,1]
print(findSmallestMissingPositiveNumber(arr))     
    