game_player_cnt = 0

n, g = map(str, input().split())

if g == "Y":
    game_player_cnt = 2
elif g == "F":
    game_player_cnt = 3
elif g == "O":
    game_player_cnt = 4

cnt = 0
ans = 0
played = set()
for _ in range(int(n)):
    name = input()

    if name not in played:
        played.add(name)
        cnt += 1

        if cnt == game_player_cnt - 1:
            ans += 1
            cnt = 0
            
print(ans)