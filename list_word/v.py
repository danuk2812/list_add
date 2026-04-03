def unique(numbers):
    for i in range(len(numbers)):
        if numbers.count(numbers[i])==1:
            return numbers[i]
    return None
print(unique([1,1,4,3,3,3]))