"""
 Find sum of all elements in array.
 
 Approach:
 Iterate through the list and keep adding each element to a running sum.
 
 Time Complexity : O(n)
 Space Complexity : O(n)
"""




def sumOfAllElements(arr):
    sum =0
    for num in arr:
        sum += num
        
    return sum

arr =[10,20,30,40,50]
print(sumOfAllElements(arr))
        