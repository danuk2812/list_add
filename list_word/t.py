def find_diff(numbers):
    pairs = 0
    for i in range(len(numbers)):
        first_time = True
        for j in range(i):
            if numbers[i] == numbers[j]:
                first_time=False
                break
        if first_time:
            pairs+=1
    return pairs
print(find_diff([3,2,1,2,3]))