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


"""
  Find All indices with given sum.
    
  Time Complexity = O(n)
  Space Complexity = O(n)
      
"""

def findAllIndicesWithGivenSum(arr2,sum):
    seen ={}
    pairs=[]
    
    for i,num in enumerate(arr2):
        complement = sum - num
        if complement in seen :
            for idx in seen[complement]:
                pairs.append((idx,i))
                
        if num in seen:
            seen[num].append(i)
        
        else:
            seen[num] =[i]
        
             
    return pairs
arr2=[2,7,11,15,8,1]
sum =9
print(findAllIndicesWithGivenSum(arr2,sum))





