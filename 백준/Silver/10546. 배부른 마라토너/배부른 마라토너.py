import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
entry = defaultdict(int)

for _ in range(n):
    entry[input()] += 1

for _ in range(n - 1):
    entry[input()] -= 1

for k, v in entry.items():
    if v == 1:
        print(k)
        break