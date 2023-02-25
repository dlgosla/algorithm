from collections import deque

# target_chanel = map(int, list(input()))
target_chanel = int(input())

wrong_number_count = int(input())

breaked_numbers = []
breaked_numbers.extend(list(map(int, input().split())))


dq = deque([(target_chanel, 0)])

while dq:
    chanel, count = dq.popleft()
    # print(chanel, count)

    # if chanel == target_chanel:
    #     print(count)
    #     break

    found = True
    for breaked_number in breaked_numbers:
        if str(breaked_number) in list(str(chanel)):
            dq.append((chanel - 1, count + 1))
            dq.append((chanel + 1, count + 1))
            found = False

    if found:
        print(count + len(list(str(chanel))))
        break
