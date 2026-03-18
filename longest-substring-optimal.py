class Solution:
    """ Function to find the longest substring
        without repeating characters """
    def longestNonRepeatingSubstring(self, s):
        n = len(s)
        
        # Assuming all ASCII characters
        HashLen = 256
        
        """ Hash table to store last
            occurrence of each character """
        hash = [-1] * HashLen
        
        """ Initialize hash table with
            -1 (indicating no occurrence) """
        for i in range(HashLen):
            hash[i] = -1

        l, r, maxLen = 0, 0, 0
        while r < n:
            """ If current character s[r] 
                is already in the substring """
            if hash[ord(s[r])] != -1:
                """ Move left pointer to the right
                    of the last occurrence of s[r] """
                l = max(hash[ord(s[r])] + 1, l)
            
            # Calculate the current substring length
            current_len = r - l + 1
            
            # Update maximum length found so far
            maxLen = max(current_len, maxLen)
            
            """ Store the index of the current
                character in the hash table """
            hash[ord(s[r])] = r
            
            # Move right pointer to next position
            r += 1
        
        # Return the maximum length found
        return maxLen

if __name__ == "__main__":
    s = "cadbzabcd"
    
    # Create an instance of the Solution class
    sol = Solution()

    result = sol.longestNonRepeatingSubstring(s)

    # Output the maximum length
    print("The maximum length is:")
    print(result)
