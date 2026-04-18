"""
   find Majority Element.
   
   Approach :
   used Moore’s Voting Algorithm to find Majority Element
   
   Time Complexity: O(n)
   Space Complexity: O(1)
          
"""





def findMajorityOfElement(arr):
    candidate = None
    count = 0
    
    #Find candidate (Moore's Voting)
    for num in arr:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
        
        

    #Verify candidate
    count = 0
    for num in arr:
        if num == candidate:
            count +=1
    
    if count > len(arr) // 2:
        return candidate
    
    return -1



arr =[1,2,3,4,5,2,2,2,2,5,6,2,2]
print(findMajorityOfElement(arr))