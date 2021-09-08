n, m = list(map(int, input().split(' ')))
# 4 6
array = list(map(int, input().split()))
# 19 15 10 17

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2 
    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
# 15