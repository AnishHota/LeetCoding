class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        arr = []
        for x in s.split(" "):
            if x.strip() != "":
                arr.append(x)

        return ' '.join(arr[::-1])
