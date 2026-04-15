def occuranceOfEachElement(arr):
    """
    Returns frequency of each element in array.
    Approach: HashMap / Dictionary
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    
    freq = {}
    
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    return freq


arr = [12,23,34,23,12,45,46,12,34,45,26]
print(occuranceOfEachElement(arr))