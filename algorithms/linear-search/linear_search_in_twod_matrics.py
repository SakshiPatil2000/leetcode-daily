"""
   Find element in matrix.
   
   Approach : 
   Traverse each row of the matrix
   Traverse each column inside the row
   Compare each element with target
   If found → return True
   
   Time Complexity: O(n * m)
   Space Complexity: O(1)    
    
"""


def findElementInMatrix(matrix,target):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
          if matrix[i][j]==target:
             return True
        
    return False


matrix=[[1,2,3],[4,5,6]]

target =5

print(findElementInMatrix(matrix,target))    