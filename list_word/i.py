def similar(numbers,num):
   return min(numbers,key=lambda x:abs(x-num))
print(similar([6,5,4,2,1],9))