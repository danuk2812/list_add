def bigger(numbers):
    arr=[]
    for i in range(len(numbers)):
        if numbers[i]>numbers[i-1]:
            arr.append(numbers[i])
    return arr
print(bigger([1 ,5, 2, 4, 3]))