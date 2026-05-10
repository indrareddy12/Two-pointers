class Solution:
    def minWindow(self, s: str, t: str) -> str:

        hash_map = {}

        # frequency of characters in t
        for ch in t:
            hash_map[ch] = hash_map.get(ch, 0) + 1

        l = 0
        r = 0
        cnt = 0

        min_len = float('inf')
        start_index = -1

        while r < len(s):

            # if character is needed
            if s[r] in hash_map and hash_map[s[r]] > 0:
                cnt += 1

            # reduce frequency
            if s[r] in hash_map:
                hash_map[s[r]] -= 1

            # when all characters matched
            while cnt == len(t):

                # update minimum window
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    start_index = l

                # remove left character
                if s[l] in hash_map:
                    hash_map[s[l]] += 1

                    # important character removed
                    if hash_map[s[l]] > 0:
                        cnt -= 1

                l += 1

            r += 1

        if start_index == -1:
            return ""

        return s[start_index:start_index + min_len]
