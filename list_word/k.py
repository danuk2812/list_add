def different(numbers):
    count=0
    for i in range(len(numbers)):
        if numbers[i-1]!=numbers[i]:
            count+=1
    return count
print(different([1,4,2,8,9,0]))