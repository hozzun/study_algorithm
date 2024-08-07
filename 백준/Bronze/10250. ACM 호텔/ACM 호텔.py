T = int(input())

for tc in range(T):
    H, W, N = map(int, input().split())

    count = 0
    answer = 0
    for j in range(1, W+1):
        for i in range(1, H+1):
            if j >= 10:
                room = str(i) + str(j)

            else:
                room = str(i) + "0" + str(j)

            count += 1

            if count == N:
                answer = int(room)
                break

    print(answer)