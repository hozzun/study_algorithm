import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
word = Counter(input().rstrip() for _ in range(n))

filter_word = [(k, v) for k, v in word.items() if len(k) >= m]
filter_word.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

for ans, _ in filter_word:
    print(ans)