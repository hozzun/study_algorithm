n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()
low = 1
high = house[-1] - house[0]
ans = 0
while low <= high:
    mid = (low + high) // 2
    wifi = 1
    last_wifi = house[0]
    for i in range(1, n):
        if house[i] - last_wifi >= mid:
            wifi += 1
            last_wifi = house[i]
    if wifi >= c:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1
print(ans)