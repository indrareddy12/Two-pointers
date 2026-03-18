class Solution:
    # Function to find the longest subarray with at most k zero flips
    def longestOnes(self, nums, k):
        # Left pointer for the window
        left = 0

        # Counter for zeros in the window
        zeros = 0

        # Variable to store max window length
        max_len = 0

        # Right pointer iterates through array
        for right in range(len(nums)):

            # If current element is 0, increment zero counter
            if nums[right] == 0:
                zeros += 1

            # If number of zeros > k, shrink window from left
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                # Move left pointer forward
                left += 1  

            # Update the max valid window length
            max_len = max(max_len, right - left + 1)

        # Return the result
        return max_len

# Driver code
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2

    # Output the result
    print(sol.longestOnes(nums, k))
