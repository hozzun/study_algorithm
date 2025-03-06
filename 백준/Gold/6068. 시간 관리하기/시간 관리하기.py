n = int(input())
arr = []
for _ in range(n):
    t, s = map(int, input().split())
    arr.append((t, s))
arr.sort(key=lambda x: x[1], reverse=True)

t = arr[0][1]
for s, e in arr:
    if t > e:
        t = e
    t -= s

if t < 0:
    print(-1)
else:
    print(t)