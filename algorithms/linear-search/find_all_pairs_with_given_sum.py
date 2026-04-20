"""
  Find All pairs with given sum.
  
  Approach :
  Use a hash set to store visited numbers. For each element, compute its complement (target - num).
  If complement exists in the set, we found a pair. This avoids nested loops.
  
  Time Complexity = O(n)
  Space Complexity = O(n)
      
"""

def findAllPairsWithGivenSum(arr,total):
    seen =set()
    pairs =[]
    
    for num in arr:
        complement = total - num 
        if complement in seen:
            pairs.append((num,complement))
            
        seen.add(num)
            
    return pairs

arr=[1,2,3,4,5,6,3,4,1]
target=6
print(findAllPairsWithGivenSum(arr,target))





