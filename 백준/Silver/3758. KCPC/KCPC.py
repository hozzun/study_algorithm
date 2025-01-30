T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    scores = [[0] * (k + 1) for _ in range(n + 1)]
    count = [0] * (n + 1)
    last_time = [0] * (n + 1)
    for time in range(1, m + 1):
        i, j, s = map(int, input().split())
        scores[i][j] = max(scores[i][j], s)
        count[i] += 1
        last_time[i] = time

    team_ranks = []
    for team_id in range(1, n + 1):
        total_score = sum(scores[team_id])
        team_ranks.append((total_score, count[team_id], last_time[team_id], team_id))
    team_ranks.sort(key=lambda x: (-x[0], x[1], x[2]))

    for rank, team in enumerate(team_ranks, start=1):
        if team[3] == t:
            print(rank)
            break