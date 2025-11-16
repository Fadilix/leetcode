class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s) - 1

        vowels = ["a", "e", "i", "o", "u"]
        
        rev = list(s)

        while i < j:
            if s[i].lower() not in vowels:
                i += 1
            if s[j].lower() not in vowels:
                j -= 1
            
            if s[i].lower() in vowels and s[j].lower() in vowels:
                rev[i], rev[j] = rev[j], rev[i]
                i += 1
                j -= 1
        return "".join(rev)