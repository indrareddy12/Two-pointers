class Solution:
    # Function to find longest subarray with at most k zero flips
    def longestOnes(self, nums, k):
        # Variable to store max length
        max_len = 0

        # Loop over all possible start indices
        for i in range(len(nums)):

            # Counter for zeros
            zeros = 0

            # Loop over all possible end indices
            for j in range(i, len(nums)):

                # Increment zero counter if current element is 0
                if nums[j] == 0:
                    zeros += 1

                # If number of zeros exceeds k, break
                if zeros > k:
                    break

                # Update max length if valid
                max_len = max(max_len, j - i + 1)

        # Return the longest valid subarray length
        return max_len

# Driver code
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2

    # Output the result
    print(sol.longestOnes(nums, k))
