import time
#Solution 1: Brute Force
#Time Complexity: O(n^3)
#Space Complexity: O(n) -> exceeds memory limit in extreme cases(986/987 test cases passed)
class Solution1(object): 
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if 0 <= len(s) <= 5 * 10**4:
            substrings = []
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    substrings.append(s[i:j])
            
            sortedMax_substr = sorted(substrings, key=len, reverse=True)
            valid = []
            
            for substr in sortedMax_substr:
                if self.noDuplicates(substr):
                    valid.append(substr)
            
            # Fix: Prevent IndexError by checking if valid is empty
            result = len(valid[0]) if valid else 0
        else:
            result = 0
        
        return result

    def noDuplicates(self, substr):
        d = {}
        for c in substr:
            d[c] = d.get(c, 0) + 1
        
        for count in d.values():
            if count > 1:
                return False
        return True

#Solution 2: Sliding Window
#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #s = "abcabcbb"
        if 0 <= len(s) <= 5 * 10**4:
            left = 0
            right = 0
            max_length = 0
            char_set = set() 
            
            for right in range(len(s)): 
                while s[right] in char_set: 
                    char_set.remove(s[left]) 
                    left += 1 
                char_set.add(s[right]) 
                max_length = max(max_length, right - left + 1) 
            return max_length
# Testing
print("Solution 1:")
start_time = time.time()
sol1 = Solution1()
print(sol1.lengthOfLongestSubstring(""))  # Expected output: 0
print(sol1.lengthOfLongestSubstring("abcabcbb"))  # Expected output: 3
print(sol1.lengthOfLongestSubstring("bbbbbb"))  # Expected output: 1
print(sol1.lengthOfLongestSubstring("pwwkew"))  # Expected output: 3
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")

print("Solution 2:")
start_time = time.time()
sol2 = Solution2()
print(sol2.lengthOfLongestSubstring(""))  # Expected output: 0
print(sol2.lengthOfLongestSubstring("abcabcbb"))  # Expected output: 3
print(sol2.lengthOfLongestSubstring("bbbbbb"))  # Expected output: 1
print(sol2.lengthOfLongestSubstring("pwwkew"))  # Expected output: 3
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")