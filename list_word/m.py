def reverse(numbers):
    n=len(numbers)
    for i in range(n//2):
        numbers[i],numbers[n-1-i]=numbers[n-1-i],numbers[i]
    return numbers
print(reverse([1,2,3,4,5]))