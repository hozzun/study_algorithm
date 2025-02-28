from itertools import combinations

L, C = map(int, input().split())
arr = list(map(str, input().split()))
mo_arr = ['a', 'e', 'i', 'o', 'u']

alpha = []
for i in combinations(sorted(arr), L):
    alpha.append(''.join(i))

for i in range(len(alpha)):
    mo = 0
    ja = 0
    for j in range(L):
        if alpha[i][j] in mo_arr:
            mo += 1
        else:
            ja += 1

    if mo >= 1 and ja >= 2:
        print(alpha[i])