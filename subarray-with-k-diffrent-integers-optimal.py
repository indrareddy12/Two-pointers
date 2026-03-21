class Solution:
    # Helper function to count subarrays with at most K distinct integers
    def atMostK(self, nums, K):
        freq = {}
        left = 0
        count = 0

        # Traverse the array with right pointer
        for right in range(len(nums)):
            if nums[right] not in freq or freq[nums[right]] == 0:
                K -= 1
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # Shrink the window if K becomes negative
            while K < 0:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    K += 1
                left += 1

            count += (right - left + 1)

        return count

    # Main function to return number of subarrays with exactly K distinct integers
    def subarraysWithKDistinct(self, nums, k):
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

# Driver code
sol = Solution()
nums = [1, 2, 1, 2, 3]
k = 2
print(sol.subarraysWithKDistinct(nums, k))
