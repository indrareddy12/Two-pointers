class Solution:
    # Function to find longest subarray with at most k zero flips
    def longestOnes(self, nums, k):
        # Left pointer of the window
        left = 0

        # Counter for zeros in current window
        zerocount = 0

        # Variable to store maximum valid window size
        maxlen = 0

        # Right pointer to expand window
        for right in range(len(nums)):

            # Increment zerocount if element is 0
            if nums[right] == 0:
                zerocount += 1

            # If zerocount exceeds k, shrink from left
            if zerocount > k:
                if nums[left] == 0:
                    zerocount -= 1
                # Move left pointer forward
                left += 1  

            # Update maxlen with current window size
            maxlen = max(maxlen, right - left + 1)

        # Return the result
        return maxlen

# Driver code
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2

    # Output the result
    print(sol.longestOnes(nums, k))
