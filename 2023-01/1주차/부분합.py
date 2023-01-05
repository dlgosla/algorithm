n, s = map(int, input().split())

sequence = list(map(int, input().split()))

start = 0
end = 0
sub_sum = sequence[0]

min_length = float("inf")
len_seq = len(sequence)
while start <= end:
    if end == len_seq:
        break
    # 현재 값이 더 작으면 늘려야함
    if sub_sum < s:
        end += 1
        if end < len_seq:
            sub_sum += sequence[end]

    else:
        curr_length = end - start + 1
        if curr_length < min_length:
            min_length = curr_length

        sub_sum -= sequence[start]
        start += 1

if min_length == float("inf"):
    min_length = 0
print(min_length)
