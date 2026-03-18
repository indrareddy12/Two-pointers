class Solution:
    # Function to find the maximum score by checking all front/back picks
    def maxScore(self, cardPoints, k):
        # Get total number of cards
        n = len(cardPoints)

        # Track the best score
        max_sum = 0

        # Try all combinations of i from front and k-i from back
        for i in range(k + 1):
            # Initialize current combination sum
            temp_sum = 0

            # Take i cards from front
            for j in range(i):
                temp_sum += cardPoints[j]

            # Take (k - i) cards from back
            for j in range(k - i):
                temp_sum += cardPoints[n - 1 - j]

            # Update max score if needed
            max_sum = max(max_sum, temp_sum)

        # Return the maximum score obtained
        return max_sum

# Driver code
sol = Solution()
cards = [1, 2, 3, 4, 5, 6, 1]
k = 3
print(sol.maxScore(cards, k))
