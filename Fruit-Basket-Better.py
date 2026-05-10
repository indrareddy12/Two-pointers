from collections import defaultdict

class Solution:
    # Function to find the maximum number of fruits we can collect with at most two fruit types
    def totalFruit(self, fruits):
        # Dictionary to count each fruit type in current window
        basket = defaultdict(int)
        
        # Initialize pointers and result
        left = 0
        max_fruits = 0

        # Traverse the fruits array using right pointer
        for right in range(len(fruits)):
            # Add current fruit to basket
            basket[fruits[right]] += 1

            # If more than 2 types, shrink window from left
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            # Update max result
            max_fruits = max(max_fruits, right - left + 1)

        # Return result
        return max_fruits

# Driver code
if __name__ == "__main__":
    obj = Solution()
    fruits = [1, 2, 1, 2, 3]
    print(obj.totalFruit(fruits))
