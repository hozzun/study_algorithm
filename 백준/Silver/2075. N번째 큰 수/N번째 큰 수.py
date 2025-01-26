import heapq

n = int(input())
heap = []
for _ in range(n):
        row = list(map(int, input().split()))
        for i in row:
            heapq.heappush(heap, i)
            if len(heap) > n:
                heapq.heappop(heap)
print(heap[0])