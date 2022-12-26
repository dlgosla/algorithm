def solur():

    return


n, m = map(int, input().split())
# videos = [int(length) for length in input().split()]
videos = []

max_length = 0
length_sum = 0
for length in input().split():
    length = int(length)
    if max_length < length:
        max_length = length
    length_sum += length
    videos.append(length)

start = max_length
end = length_sum
# mid = max_length + length_sum // 2

while start < end:
    mid = (end + start) // 2
    bluray_count = 1
    sub_sum = 0
    for video_length in videos:
        if sub_sum + video_length > mid:
            bluray_count += 1
            sub_sum = video_length
        else:
            sub_sum += video_length

    # print(start, end, bluray_count, mid)
    if bluray_count <= m:
        end = mid
    else:
        start = mid + 1

print(start)
