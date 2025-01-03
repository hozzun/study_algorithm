from collections import defaultdict

N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]

sushi_dict = defaultdict(int)
unique_cnt = 0
max_cnt = 0

for i in range(k):
    if sushi_dict[belt[i]] == 0:
        unique_cnt += 1
    sushi_dict[belt[i]] += 1

max_cnt = unique_cnt + (1 if sushi_dict[c] == 0 else 0)

for i in range(N):
    new_sushi = belt[(i+k) % N]
    if sushi_dict[new_sushi] == 0:
        unique_cnt += 1
    sushi_dict[new_sushi] += 1

    old_sushi = belt[i]
    sushi_dict[old_sushi] -= 1
    if sushi_dict[old_sushi] == 0:
        unique_cnt -= 1

    max_cnt = max(max_cnt, unique_cnt + (1 if sushi_dict[c] == 0 else 0))

print(max_cnt)