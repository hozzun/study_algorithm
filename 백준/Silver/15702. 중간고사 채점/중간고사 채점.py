from collections import defaultdict

n, m = map(int, input().split())
scores = list(map(int, input().split()))

grid = [list(map(str, input().split())) for _ in range(m)]

answer = defaultdict(int)
testers = []
for i in range(m):
    testers.append(int(grid[i][0]))
    for j in range(1, n + 1):
        if grid[i][j] == 'O':
            answer[int(grid[i][0])] += scores[j - 1]

min_tester = float('inf')
max_score = float('-inf')

if not answer:
    print(min(testers), 0)
else:
    for k, v in answer.items():
        if max_score < v:
            max_score = v
            min_tester = k
        elif max_score == v and min_tester > k:
            min_tester = k

    print(min_tester, max_score)