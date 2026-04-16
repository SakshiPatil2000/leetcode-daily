"""
 Find element in list of array.  
 
 Approach :   
 Traverse each element in the array one by one.If element matches the target then return true.
 
 Time Complexity : O(n)
 Spce Complexity : O(1)
 
"""



def findElementInArray(arr,target):
    for ch in arr:
        if ch == target:
            return True
        
    return False

arr=["sakshi","python","react","flutter"]
target="python"
print(findElementInArray(arr,target))