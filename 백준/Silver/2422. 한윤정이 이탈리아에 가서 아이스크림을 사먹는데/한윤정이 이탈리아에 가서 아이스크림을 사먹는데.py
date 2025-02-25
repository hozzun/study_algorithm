n, m = map(int, input().split())
icecream = set()
for _ in range(m):
    a, b = map(int, input().split())
    icecream.add((a, b))
    icecream.add((b, a))

count = 0
for a in range(1, n - 1):
    for b in range(a + 1, n):
        for c in range(b + 1, n + 1):
            if (a, b) in icecream or (b, c) in icecream or (a, c) in icecream:
                continue
            count += 1

print(count)