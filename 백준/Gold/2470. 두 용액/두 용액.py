n = int(input())
solution = list(map(int, input().split()))
solution.sort()
left = 0
right = n - 1
target_sum = float('inf')
result = None
while left < right:
    cur_sum = solution[left] + solution[right]
    if abs(cur_sum) < abs(target_sum):
        target_sum = cur_sum
        result = (solution[left], solution[right])
    if cur_sum == 0:
        result = (solution[left], solution[right])
        break
    if cur_sum < 0:
        left += 1
    else:
        right -= 1
print(result[0], result[1])