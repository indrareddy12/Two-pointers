class Solution:
    # Function to return maximum score by picking k cards from either end
    def maxScore(self, cardPoints, k):
        # Get total number of cards
        n = len(cardPoints)

        # Calculate initial sum from first k cards
        total = sum(cardPoints[:k])

        # Initialize max score with initial total
        maxPoints = total

        # Slide the window: remove from front, add from back
        for i in range(k):
            # Subtract from the front
            total -= cardPoints[k - 1 - i]

            # Add from the back
            total += cardPoints[n - 1 - i]

            # Update max score
            maxPoints = max(maxPoints, total)

        # Return the maximum score
        return maxPoints

# Driver code
cards = [1, 2, 3, 4, 5, 6, 1]
k = 3
sol = Solution()
print(sol.maxScore(cards, k))
