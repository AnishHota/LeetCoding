class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sfreq = collections.Counter(s)
        tfreq = collections.Counter(t)

        if sfreq==tfreq:
            return True
        
        return False
        