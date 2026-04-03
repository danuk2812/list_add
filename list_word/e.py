def first_plus(numbers):
    i=0
    try:
        while numbers[i]<=0:
            i+=1
        return i
    except IndexError:
        return -1
print(first_plus([0,-1,2]))