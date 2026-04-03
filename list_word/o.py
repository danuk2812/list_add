def min_max(numbers):
    index_max = numbers.index(max(numbers))
    index_min = numbers.index(min(numbers))
    numbers[index_max],numbers[index_min]=numbers[index_min],numbers[index_max]
    return numbers
print(min_max([3,4,5,2,1]))