"""
  find an index where left sum = right sum.
  
  Approach : Equilibrium Index / Pivot Index
  formula => 2×LeftSum+arr[i]=TotalSum
  
  Time Complexity = O(n)
  Space Complexity =O(n)
      
"""

def findEquilibriumIndex(arr):
    totalSum= sum(arr)
    leftSum = 0
    for i in range(len(arr)):
         if 2*leftSum + arr[i] == totalSum:
             return i
         leftSum += arr[i]
         
    return -1


arr =[2,1,1,1] 
print(findEquilibriumIndex(arr))