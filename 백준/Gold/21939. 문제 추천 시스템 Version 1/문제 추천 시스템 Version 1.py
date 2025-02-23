import heapq

n = int(input())

min_heap = []
max_heap = []
problems = {}
solved = set()

for _ in range(n):
    p, l = map(int, input().split())
    heapq.heappush(min_heap, (l, p))
    heapq.heappush(max_heap, (-l, -p))
    problems[p] = l

m = int(input())
for _ in range(m):
    command = input().split()

    if command[0] == 'recommend':
        x = int(command[1])
        if x == 1:
            while max_heap:
                l, p = max_heap[0]
                l, p = -l, -p
                if p not in solved and problems[p] == l:
                    print(p)
                    break
                heapq.heappop(max_heap)

        else:
            while min_heap:
                l, p = min_heap[0]
                if p not in solved and problems[p] == l:
                    print(p)
                    break
                heapq.heappop(min_heap)

    elif command[0] == 'add':
        p, l = int(command[1]), int(command[2])
        heapq.heappush(min_heap, (l, p))
        heapq.heappush(max_heap, (-l, -p))
        problems[p] = l
        if p in solved:
            solved.remove(p)

    else:
        p = int(command[1])
        solved.add(p)