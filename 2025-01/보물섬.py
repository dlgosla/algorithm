from collections import deque

r, c = map(int, input().split())


map = [[0]*c for _ in range(r)]

for i in range(r):
    for j,item in enumerate(list(input())):
        if (item == 'W'):
            map[i][j] = 1

dr = [1,0,-1,0]
dc = [0,-1,0,1]

max_distance = 0
for i in range(r):
    for j in range(c):
        # distance = [[float('inf')]*c for _ in range(r)]
        if map[i][j] == 0:
            temp_max = 0
            visited = [[0]*c for _ in range(r)]
            visited[i][j] = 1
            dq = deque()
            dq.append((i,j, 0))

            while dq:
                cr, cc, cd  = dq.popleft()
                for dr_, dc_ in zip(dr, dc):
                    nr = cr + dr_
                    nc = cc + dc_
                    nd = cd +1

                    if (0<=nr<r and 0 <= nc <c) and map[nr][nc] == 0 and not visited[nr][nc]:
                        visited[nr][nc] = 1
                        dq.append((nr,nc, nd))
                        # if (distance[nr][nc] > nd):
                        #     distance[nr][nc] = nd
                        if (temp_max < nd):
                            temp_max = nd
            
            max_distance = max(temp_max, max_distance)
            #print(distance)
            #min_num = max(map(max, distance))
print(max_distance)

            
