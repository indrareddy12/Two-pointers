class Solution:
    # Function to calculate maximum fruits collected  
    # with at most two distinct types from any start point  
    def totalFruit(self, fruits):

        # Variable to store the maximum fruits collected
        max_fruits = 0

        # Loop over each possible starting point
        for start in range(len(fruits)):

            # Dictionary to count fruit types in the basket
            basket = {}

            # Variable to track number of fruits collected from this start
            current_count = 0

            # Traverse from start to end of array
            for end in range(start, len(fruits)):

                # Add current fruit to the basket
                basket[fruits[end]] = basket.get(fruits[end], 0) + 1

                # If basket has more than 2 types, break
                if len(basket) > 2:
                    break

                # Increase the current fruit count
                current_count += 1

            # Update the maximum fruits collected
            max_fruits = max(max_fruits, current_count)

        # Return the result
        return max_fruits

# Driver code
if __name__ == "__main__":
    obj = Solution()
    fruits = [1, 2, 1]
    print(obj.totalFruit(fruits))  # Output: 3
