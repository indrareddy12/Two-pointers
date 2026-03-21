class Solution:
    # Function to calculate longest substring with at most K distinct characters
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Track the maximum valid substring length
        max_len = 0

        # Try every possible starting index
        for i in range(len(s)):
            # Use dictionary to count frequencies of characters
            freq = {}

            # Expand the substring from index i
            for j in range(i, len(s)):
                # Update character frequency
                freq[s[j]] = freq.get(s[j], 0) + 1

                # If more than k distinct characters, stop expanding
                if len(freq) > k:
                    break

                # Update the maximum length
                max_len = max(max_len, j - i + 1)

        # Return the result
        return max_len

# Driver code
if __name__ == "__main__":
    sol = Solution()
    s = "eceba"
    k = 2
    print(sol.lengthOfLongestSubstringKDistinct(s, k))
