class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_store = {}
        if len(s) != len(t):
            return False

        for char in s:
            char_store[char] = char_store.get(char, 0) + 1
        
        for char in t:
            if char not in char_store or char_store[char] == 0:
                return False
            
            char_store[char] -= 1

        return True