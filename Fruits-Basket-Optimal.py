class Solution:
    # Function to find the maximum number of fruits we can collect
    # with at most two types of fruits in the baskets.
    def totalFruit(self, fruits):
        
        # Initialize variables for tracking fruit types and counts
        maxlen = 0
        lastfruit = secondlastfruit = -1
        currcount = 0
        lastfruitstreak = 0

        # Traverse through the fruits array
        for fruit in fruits:
            
            # If current fruit matches last two, increase window size
            if fruit == lastfruit or fruit == secondlastfruit:
                currcount += 1
            else:
                # Otherwise reset to streak size
                currcount = lastfruitstreak + 1

            # Update last fruit streak and tracking
            if fruit == lastfruit:
                lastfruitstreak += 1
            else:
                lastfruit_streak = 1
                secondlastfruit = lastfruit
                lastfruit = fruit

            # Update max length
            maxlen = max(maxlen, currcount)

        return maxlen

# Driver code
if __name__ == "__main__":
    sol = Solution()
    fruits = [1,2,1,2,3]
    print(sol.totalFruit(fruits))
