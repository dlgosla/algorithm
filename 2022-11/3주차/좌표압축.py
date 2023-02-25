n = int(input())

coodinates = [int(i) for i in input().split()]
sorted_coodinates = sorted([int(coodinate) for coodinate in set(coodinates)])
length = len(sorted_coodinates)

answer = []
for coodinate in coodinates:
    start = 0
    end = length
    while start <= end:
        mid = (start + end) // 2
        if sorted_coodinates[mid] == coodinate:
            answer.append(mid)
            break

        if sorted_coodinates[mid] > coodinate:
            end = mid - 1
        else:
            start = mid + 1

print(*answer)
