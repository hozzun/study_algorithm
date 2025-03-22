def f(x):
    if x == M:
        print(*arr)
        return

    for i in range(1, N+1):
        if i in arr:
            continue
        if arr and i < arr[-1]:
            continue
        arr.append(i)
        f(x + 1)
        arr.pop()

N, M = map(int, input().split())
arr = []
f(0)