N = int(input())
result = 0
for tc in range(N):
    word = input()
    cnt = ''

    if len(word) == 1 or len(word) == 2:
        result += 1

    else:
        for i in word:
            if i not in cnt:
                cnt += i
            elif i in cnt:
                if cnt[-1] == i:
                    cnt += i
                elif cnt[-1] != i:
                    break
        if word == cnt:
            result += 1

print(result)