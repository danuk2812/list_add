def max_index(numbers):
    max_number=max(numbers)
    index_max=numbers.index(max_number)
    return f"{max_number} {index_max}"
print(max_index([1,2,3,3,1]))