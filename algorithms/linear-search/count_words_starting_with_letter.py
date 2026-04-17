"""
   Count how many words in the list start with a given letter.
   
   Approach :
   Traverse each word in the array.
   Check the first character of each word (ch[0]).
   If it matches the given letter, increment the counter.
   Return the final count after checking all words.
   
   Time Complexity: O(n) 
   Space Complexity: O(1) → no extra space used
   
"""


def countWordsStartingWithletters(arr,letter):
    count =0
    for ch in arr:
        if ch[0] == letter:
            count +=1
    return count

arr=["sakshi","shree","vicky","python"]
letter='s'
print(countWordsStartingWithletters(arr,letter))
    