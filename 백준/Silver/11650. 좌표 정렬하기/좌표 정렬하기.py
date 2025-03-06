T = int(input())

lst = []
for tc in range(T):
    x, y = map(int, input().split())
    lst.append((x, y))

lst.sort()

for _ in lst:
    print(*_)