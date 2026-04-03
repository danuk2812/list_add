def even(numbers):
    arr=[]
    for i in range(len(numbers)):
        if numbers[i]%2==0:
            arr.append(numbers[i])
    return arr
print(even([1, 2, 2, 3, 3, 3 ,4]))