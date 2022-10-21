class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[] for i in range(numRows)]

        r, c = 0, 0

        dr = [1, -1]
        dc = [0, 1]

        direction = 0

        for char in s:
            matrix[r].append(char)

            nr = r + dr[direction]
            nc = c + dc[direction]

            if not 0 <= nr < numRows:
                direction = (direction + 1) % 2
                r += dr[direction]
                c += dc[direction]

            else:
                r = nr
                c = nc

        answer = ""
        for elem in matrix:
            answer += "".join(elem)

        print(answer)
        return answer
