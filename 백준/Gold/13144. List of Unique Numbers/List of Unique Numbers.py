from collections import defaultdict

n = int(input())
sequence = list(map(int, input().split()))

left = 0
right = 0
num_count = defaultdict(int)
answer = 0

while right < n:
    num_count[sequence[right]] += 1

    while num_count[sequence[right]] > 1:
        num_count[sequence[left]] -= 1
        left += 1

    answer += (right - left + 1)
    right += 1

print(answer)