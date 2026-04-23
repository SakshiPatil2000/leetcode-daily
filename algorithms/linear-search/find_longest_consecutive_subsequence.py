"""
   Find longest consecutive subsequence.
   
   Approach:
   Store elements in set
   Find the start of the subsequence
   Expand the sequence forward
   Track max length   
   Return result
   
   Time Complexity : O(n)
   Space Complexity : O(n)
   
"""


def longestConsecutive(arr):
    numSet = set(arr)
    longest = 0

    for num in numSet:
        # check if it is start of sequence
        if num - 1 not in numSet:
            length = 1
            while num + length in numSet:
                length += 1
            longest = max(longest, length)

    return longest

arr = [100,4,200,1,3,2]
print(longestConsecutive(arr))