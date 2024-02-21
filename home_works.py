# arr = []
# for i in range(10):
#     arr.append(i)
# print(*arr[::-1])
# arr = arr[::-1]
# count = 0
# while count < len(arr):
#    chislo = arr[count]
#    if chislo % 2 == 0:
#        print(f'{chislo} even')
#    else:
#        print(f'{chislo} not even')
#    count+=1
arr = [i for i in range(10)]
print(*arr[::-1])
for item in arr:
    if item % 2 == 0:
        print(f'{item} is add')
    else:
        print(f"{item} is even")