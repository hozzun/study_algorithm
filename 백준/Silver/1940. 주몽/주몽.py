N = int(input())
M = int(input())
arr = list(map(int, input().split()))

arr.sort()

ans = 0
cur_sum = 0
left = 0
right = N-1
while left < right:
    cur_sum = arr[left] + arr[right]

    if cur_sum == M:
        ans += 1
        left += 1
        right -= 1
    elif cur_sum < M:
        left += 1
    else:
        right -= 1

print(ans)