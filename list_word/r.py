def find_pairs(numbers):
    pairs = 0
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]==numbers[j]:
                pairs+=1
    return pairs
print(find_pairs([1,2,3,2,3]))