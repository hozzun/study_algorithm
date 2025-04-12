import sys

N = int(sys.stdin.readline())
score_lst = list(map(int, sys.stdin.readline().split()))
max_score = max(score_lst)

cal_lst = []
for i in score_lst:
    cal_lst.append(i/max_score*100)

avg = sum(cal_lst)/N
print(avg)