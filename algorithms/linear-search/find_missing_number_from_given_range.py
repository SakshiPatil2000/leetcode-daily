def findMissingNumberFromGivenRange(arr,start,end):
    expected_sum = (end *(end+1) //2) - (start * (start-1) //2)
    actual_sum= sum(arr)
    
    return expected_sum -actual_sum

arr =[11,12,13,14,16,17,18,19,20]
start =11
end = 20

print(findMissingNumberFromGivenRange(arr,start,end))