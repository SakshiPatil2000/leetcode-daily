"""
    Approach:
    We use Linear Search to traverse each character of the string.
    For every character, we check whether it is present in the
    vowel string "aeiouAEIOU". If yes, we increment the counter.

    Time Complexity:
    O(n) → We scan the string once, where n = length of string.

    Space Complexity:
    O(1) → No extra space used except a counter variable.
    
"""


def countVowels(str):
    vowels ="aeiouAEIOU"
    count =0
    for ch in str:
        if ch in vowels:
            count +=1
    return count

name = "Elephant"
print(countVowels(name))