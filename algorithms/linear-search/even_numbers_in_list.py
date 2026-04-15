""" 
 Find even numbers from the list.
 
 Approach :
 Iterate through the list and check each number.
 If number % 2 == 0, add it to the result list.
 
 Time Complexity : O(n)
 Space Complexity : O(K)


"""



def evenNumbers(arr):
    even=[]
    
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even.append(arr[i])
            
    return even 

arr = [10,12,13,15,16,17,19,21]
print(evenNumbers(arr))