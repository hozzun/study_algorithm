from itertools import combinations

while True:
    data = input().split()
    k = int(data[0])
    if k == 0:
        break
    s = list(map(int, data[1:]))

    for combo in combinations(s, 6):
        print(' '.join(map(str, combo)))
    print()