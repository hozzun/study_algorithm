n, m = map(int, input().split())
preferences = [list(map(int, input().split())) for _ in range(n)]

max_val = 0
for i in range(m):
    for j in range(i + 1, m):
        for k in range(j + 1, m):
            total = 0
            for preference in preferences:
                max_preference = max(preference[i], preference[j], preference[k])
                total += max_preference
            max_val = max(max_val, total)

print(max_val)