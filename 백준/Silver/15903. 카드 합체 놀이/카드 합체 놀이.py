import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)

for i in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)

    temp = x + y
    heapq.heappush(cards, temp)
    heapq.heappush(cards, temp)

print(sum(cards))