n, l = map(int, input().split())
locations = list(map(int, input().split()))
locations.sort()

answer = 0
end = 0
for location in locations:
    if location > end:
        answer += 1
        end = (location - 0.5) + l

print(answer)