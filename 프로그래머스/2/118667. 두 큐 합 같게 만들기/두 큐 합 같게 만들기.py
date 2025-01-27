from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    cnt = 0
    limit = len(q1) * 5
    total = sum1 + sum2
    target = total // 2
    if total % 2 != 0:
        return -1
    while sum1 != target and cnt < limit:
        if sum1 > target:
            v = q1.popleft()
            sum1 -= v
            q2.append(v)
        else:
            v = q2.popleft()
            sum2 -= v
            q1.append(v)
            sum1 += v
        cnt += 1
    return cnt if sum1 == target else -1