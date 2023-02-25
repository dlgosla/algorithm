class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        mid = length // 2

        # dp = [0] * length

        idx = 1
        max_length = 0
        peline = ""

        while True:
            if idx == length - 1:
                break

            next_idx = idx + 1
            prev_idx = idx - 1
            idx = idx

            start = 0
            end = 0

            print(prev_idx, next_idx)

            peline_length = 0

            if s[idx] == s[next_idx]:
                next_idx += 1
                start = idx
                end = idx + 1

            while True:
                if prev_idx - 1 < 0 or next_idx + 1 >= length:
                    peline_length = next_idx - prev_idx + 1
                    start = prev_idx
                    end = next_idx
                    break

                # print(prev_idx, next_idx)
                if s[prev_idx - 1] == s[next_idx + 1]:
                    prev_idx -= 1
                    next_idx += 1

                else:
                    break

            # print(prev_idx, next_idx, idx)

            if max_length < peline_length:
                max_length = peline_length
                peline = s[start : end + 1]

            if peline_length == length:
                break

            idx += 1

        # print(peline)

        return peline
