def solution(a, d, included):
    seq = []
    cur = a
    
    for i in range(len(included)):
        seq.append(cur)
        cur += d

    answer = 0
    for idx, ic in enumerate(included):
        if ic:
            answer += seq[idx]
            
    return answer