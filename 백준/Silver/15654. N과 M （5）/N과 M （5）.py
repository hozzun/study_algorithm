def f(x):
    if x == M:
        print(*arr)
        return

    for i in range(N):
        if N_num[i] in arr:
            continue
        arr.append(N_num[i])
        f(x + 1)
        arr.pop()

N, M = map(int, input().split())
N_num = list(map(int, input().split()))
N_num.sort()
arr = []
f(0)
