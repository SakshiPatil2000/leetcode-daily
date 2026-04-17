"""
   Find the Longest Word in a List.
   
   Approach:
   Start with longest_word = None and max length = 0
   Traverse each word in the list
   If current word length is greater than max length,update longest_word and max length
   Return the longest word after loop ends
   
   Time Complexity: O(n)
   Space Complexity: O(1)
      
"""

def findLongestWord(arr):
    longest_word = None
    len_longest_word = 0
    
    for str in arr:
        if len(str) > len_longest_word:
            longest_word = str
            
    return longest_word

arr =["sakshi","shree","vicky","vishwajeet"]
print(findLongestWord(arr))