def recur(idx, dan, zi, tan, vi, price, selected):
    global min_price
    global min_num

    if price > min_price:
        return

    if dan >= mp and zi >= mf and tan >= ms and vi >= mv:
        if price < min_price:
            min_price = price
            min_num = selected[:]
        return

    if idx == N:
        return
    
    # 식재료 사용
    selected.append(idx + 1)
    recur(idx + 1, dan + arr[idx][0], zi + arr[idx][1], tan + arr[idx][2], vi + arr[idx][3], price + arr[idx][4], selected)
    selected.pop()

    # 사용 안함
    recur(idx + 1, dan, zi, tan, vi, price, selected)

N = int(input())
mp, mf, ms, mv = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

min_price = 99999999

recur(0, 0, 0, 0, 0, 0, [])
if min_price == 99999999:
    print(-1)
else:
    print(min_price)
    print(*min_num)