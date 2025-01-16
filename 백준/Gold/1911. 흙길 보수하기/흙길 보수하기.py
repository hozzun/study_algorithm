N, L = map(int, input().split())

load = []
for _ in range(N):
    s, e = map(int, input().split())
    load.append((s, e))

load.sort(key=lambda x: x[0])

ans = 0
last = 0
for s, e in load:
    if last < s:
        last = s

    if last < e:
        length = e - last
        board = (length + L - 1) // L
        ans += board
        last += board * L

print(ans)