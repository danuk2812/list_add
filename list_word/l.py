def smallest_uneven(numbers):
    uneven_numbers = [x for x in numbers if x % 2 != 0]
    if not uneven_numbers:
        return None
    return min(uneven_numbers)

print(smallest_uneven([5, 3, 1, 4]))