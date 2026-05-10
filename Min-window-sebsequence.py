class Solution:
    def minWindow(self, s1: str, s2: str) -> str:

        n = len(s1)
        m = len(s2)

        min_len = float('inf')
        ans = ""

        i = 0

        while i < n:

            j = 0

            # forward match
            while i < n:
                if s1[i] == s2[j]:
                    j += 1

                    # complete subsequence found
                    if j == m:
                        break

                i += 1

            # no valid subsequence
            if i == n:
                break

            end = i + 1

            # backward shrinking
            j = m - 1

            while i >= 0:
                if s1[i] == s2[j]:
                    j -= 1

                    # start found
                    if j < 0:
                        break

                i -= 1

            start = i

            # update answer
            if (end - start) < min_len:
                min_len = end - start
                ans = s1[start:end]

            # move ahead for next search
            i = start + 1

        return ans
