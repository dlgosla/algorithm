n = int(input())
video = []
for i in range(n):
    video.append(list(input()))


def divide(metrix):
    length = len(metrix)

    if length == 1:
        return metrix[0][0]

    if length == 0:
        return

    mid = length // 2

    results = []

    """
    [[1,0,1,1],
    [1,0,1,1],
    [1,0,1,0],
    [1,0,1,0]]

    위, 왼쪽 -> 행 [0:2], 열 [0:2] -> 행 [0:mid], 열 [0:mid]
    위, 오른쪽 -> 행 [0:2], 열 [mid:length] -> 행 [0:mid], 열[mid:length]..
    """
    # 1/4 조각 내기
    left = (0, mid)  # 왼쪽은 행이 mid이하인 곳
    right = (mid, length)  # 오른쪽은 행이 mid 이상인곳
    top = (0, mid)  # 위는 열이 mid 이하인곳
    bottom = (mid, length)

    # 왼쪽 위, 오른쪽 위, 왼쪽아래, 오른쪽 아래 순으로 쪼갤 수 있을 때 까지 4등분 반복
    """
    [[1,0,1,1],
    [1,0,1,1],
    [1,0,1,0],
    [1,0,1,0]]

    왼쪽 위
    [[1,0],
    [1,0]] 
    => [[1]], [[0]], [[1]], [[0]]
    => result = [1,0,1,0]

    오른쪽 위
    [[1,1],
    [1,1]]
    => [[1]],[[1]],[[1]],[[1]]
    => result = [1,1,1,1]
    ...
    """
    slicing_quadrant = [(top, left), (top, right), (bottom, left), (bottom, right)]
    for row, col in slicing_quadrant:
        sliced = [lst[col[0] : col[1]] for lst in metrix[row[0] : row[1]]]
        results.append(divide(sliced))

    """
    [[1,0,1,1],
    [1,0,1,1],
    [1,0,1,0],
    [1,0,1,0]]

    왼쪽 위 
    -> results = [1,0,1,0]
    -> (1010)

    오른쪽 위 
    -> results = [1,1,1,1]
    -> 1
    ...
    
    최종 병합 때는
    results = [(1010),1,(1010),(1010)]이 됨
    """
    # 사분면이 모두 1이거나 0이면
    if results == ["0"] * 4 or results == ["1"] * 4:
        # 압축
        return results[0]

    # 아니면 압축안함
    return "(" + "".join(results) + ")"


result = divide(video)
print("".join(result))
