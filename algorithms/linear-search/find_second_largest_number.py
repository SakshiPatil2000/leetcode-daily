"""
    Approach:
    We use Linear Search to traverse the array once.
    - Assume first element as the largest.
    - Whenever we find a number greater than the current largest,
      we update secondLargest as the previous largest,
      and update largest with the new maximum value.
    - After scanning the whole array, secondLargest holds the
      second biggest element.

    Time Complexity:
    O(n) → We traverse the array only once.

    Space Complexity:
    O(1) → No extra space used, only two variables are used.
    
"""


def secondLargest(arr):
    largest =arr[0]
    secondLargestNum =0
    for i in range(len(arr)):
        if arr[i] > largest :
            secondLargestNum = largest
            largest = arr[i]
            
    return secondLargestNum

arr =[10,12,15,13,16,78,24,99]
print(secondLargest(arr))
    