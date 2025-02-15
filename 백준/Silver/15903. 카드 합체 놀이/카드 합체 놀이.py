N, M = map(int, input().split())
arr = list(map(int, input().split()))

i = 0
while True:
    arr.sort()
    if i == M:
        break

    a = arr.pop(0)
    b = arr.pop(0)

    c = a + b
    arr.append(c)
    arr.append(c)

    i += 1

answer = sum(arr)
print(answer)
