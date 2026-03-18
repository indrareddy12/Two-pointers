class Solution:
    def longestNonRepeatingSubstring(self, s):
        # Length of the input string
        n = len(s)
        
        # Variable to store max length
        maxLen = 0
        
        """ Iterate through all possible 
            starting points of the substring """
        for i in range(n):
            
            """ Hash to track characters in 
                the current substring window """
            # Assuming extended ASCII characters
            hash_set = [0] * 256
            
            for j in range(i, n):
                
                """ If s[j] is already in the
                    current substring window """
                if hash_set[ord(s[j])] == 1:
                    break
                
                """ Update the hash_set to mark s[j]
                    as present in the current window """
                hash_set[ord(s[j])] = 1
                
                """ Calculate the length of
                    the current substring """
                current_len = j - i + 1
                
                """ Update maxLen if the current
                    substring length is greater """
                maxLen = max(maxLen, current_len)
        
        # Return the maximum length
        return maxLen

if __name__ == "__main__":
    
    input_str = "cadbzabcd"
    
    # Create an instance of Solution class
    sol = Solution()
    
    length = sol.longestNonRepeatingSubstring(input_str)
    
    # Print the result
    print("Length of longest substring without repeating characters:", length)
