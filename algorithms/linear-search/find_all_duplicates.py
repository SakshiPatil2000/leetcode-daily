"""
    Approach:
    We use Linear Search with a 'seen' set.
    - Traverse each element in the array.
    - If the element is already present in the seen set,
      it means we found a duplicate → add it to duplicates list.
    - Otherwise, add the element to seen set.
    - Return all duplicate elements.

    Time Complexity:
    O(n) → We traverse the array once.

    Space Complexity:
    O(n) → Extra space used for 'seen' set and duplicates list.
    
"""



def findDuplicates(arr):
    seen= set()
    duplicates=[]
    
    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

arr = [23,1,3,4,5,6,2,3,7,8,6,1]
print(findDuplicates(arr))