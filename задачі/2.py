def numbers(number):
    arr=number.split(' ')
    sum=0
    for i in arr:
        sum+=int(i)
    return sum

print(numbers('4 -10 18 16'))
