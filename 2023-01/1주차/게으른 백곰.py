from collections import defaultdict


n, k = map(int, input().split())

buckets = defaultdict(int)
end = 0
for i in range(n):
    g, x = map(int, input().split())
    buckets[x] = g
    if end < x:
        end = x

curr_sum = 0
for i in range(k):
    curr_sum += buckets[i]

max_sum = 0
for i in range(end):
    left = i - k - 1
    right = i + k

    curr_sum = curr_sum + buckets[right] - buckets[left]
    if curr_sum > max_sum:
        max_sum = curr_sum

print(max_sum)
