def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
# 5
array = list(map(int, input().split()))
# 8 3 7 9 2
array.sort()

m = int(input())
# 3
x = list(map(int, input().split()))
# 5 7 9

for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# no yes yes