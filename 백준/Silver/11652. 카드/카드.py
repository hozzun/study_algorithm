from collections import defaultdict
n = int(input())
cnt = defaultdict(int)
for _ in range(n):
    card = int(input())
    cnt[card] += 1
cnt = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
print(cnt[0][0])