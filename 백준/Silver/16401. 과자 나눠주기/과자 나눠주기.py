m, n = map(int, input().split())
cookies = list(map(int, input().split()))

answer = 0
left, right = 1, max(cookies)
while left <= right:
    mid = (left + right) // 2
    cnt = sum(i // mid for i in cookies)

    if cnt >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)