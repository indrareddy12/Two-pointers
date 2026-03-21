class Solution:
    # Function to return length of longest substring with at most K distinct characters
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Edge case
        if k == 0 or not s:
            return 0

        # Dictionary to store frequency of characters
        freq = {}

        # Initialize pointers and result
        left = 0
        maxLen = 0

        # Iterate using right pointer
        for right in range(len(s)):
            # Add current char to freq map
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Shrink window if needed
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            # Update maxLen
            maxLen = max(maxLen, right - left + 1)

        return maxLen

# Driver code
sol = Solution()
s = "eceba"
k = 2
print(sol.lengthOfLongestSubstringKDistinct(s, k))
