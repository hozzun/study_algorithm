def solve(n, x, visits):
    cur_sum = sum(visits[:x])
    max_sum = cur_sum
    max_cnt = 1
    for i in range(x, n):
        cur_sum += visits[i]
        cur_sum -= visits[i - x]
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_cnt = 1
        elif cur_sum == max_sum:
            max_cnt += 1
    if max_sum == 0:
        print("SAD")
    else:
        print(max_sum)
        print(max_cnt)

n, x = map(int, input().split())
visits = list(map(int, input().split()))
solve(n, x, visits)