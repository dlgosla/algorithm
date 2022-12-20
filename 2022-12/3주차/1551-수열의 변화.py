n, k = map(int, input().split())

a = list(map(int, input().split(",")))


for i in range(k):
    temp = []
    for j in range(len(a) - 1):
        front = a[j]
        back = a[j + 1]
        temp.append(back - front)

    a = temp[:]

print(",".join(map(str, a)))
