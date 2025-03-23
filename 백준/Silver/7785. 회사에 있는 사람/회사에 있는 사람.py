import sys
input = sys.stdin.readline

T = int(input())
enter = set()
for tc in range(1, T+1):
    a, b = input().split()
    if b == 'enter':
        enter.add(a)
    if b == 'leave':
        enter.remove(a)

result = sorted(enter, reverse=True)
print(*result, sep='\n')