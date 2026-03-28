def split(number):
    sum=0
    arr= number.split(' ')
    new_arr = arr.copy()
    new_arr.reverse()
    print(new_arr)
    for i in new_arr:
        sum+=int(i)
    return sum
print(split("2 -1 9 6"))