def smallest_add(numbers):
    add_numbers=list(filter(lambda x:x>=0,numbers))
    return min(add_numbers)
print(smallest_add([5,3,-2,-1,1]))