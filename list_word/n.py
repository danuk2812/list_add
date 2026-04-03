def neighbours (numbers):
    n=len(numbers)
    for i in range(0,n-1,2):
        numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
    return numbers
print(neighbours([1,2,3,4,5]))