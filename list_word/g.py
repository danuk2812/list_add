def neighbour(numbers):
    count=0
    for i in range(len(numbers)):
        if numbers[i-1]<=numbers[i]:
            count+=1
    return count
print(neighbour([1 ,2 ,3 ,4 ,5]))