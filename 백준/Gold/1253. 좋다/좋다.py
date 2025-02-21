n = int(input())
nums = sorted(list(map(int, input().split())))

count = 0
for i in range(n):
    target = nums[i]
    left = 0
    right = n - 1

    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        current_sum = nums[left] + nums[right]
        if current_sum == target:
            count += 1
            break
        elif current_sum < target:
            left += 1
        else:
            right -= 1

print(count)