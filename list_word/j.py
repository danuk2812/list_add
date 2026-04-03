def sherenga(height,andriy):
    i=1
    while height[i-1]>=andriy:
       i+=1
    return i
print(sherenga([165 ,163, 160, 160, 157, 157, 155, 154],157))