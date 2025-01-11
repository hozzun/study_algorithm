from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = deque([0] * w)
ans = 0
weight = 0

for truck in trucks:
    while True:
        ans += 1
        weight -= bridge.popleft()

        if weight + truck <= L:
            bridge.append(truck)
            weight += truck
            break
        else:
            bridge.append(0)

ans += w
print(ans)