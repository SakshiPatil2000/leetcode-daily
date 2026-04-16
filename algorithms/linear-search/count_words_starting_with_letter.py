def countWordsStartingWithletters(arr,letter):
    count =0
    for ch in arr:
        if ch[0] == letter:
            count +=1
    return count

arr=["sakshi","shree","vicky","python"]
letter='s'
print(countWordsStartingWithletters(arr,letter))
    