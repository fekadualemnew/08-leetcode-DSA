class Solution:
    def freqAlphabets(self, s: str) -> str:
        letters = " abcdefghijklmnopqrstuvwxyz"
        m = {}
        n = len(s)

        for i in range(1,27):
            if i <= 9:
                m[str(i)] = letters[i]
            else:
                m[str(i) + "#"] = letters[i]
        
        res = ""
        i = 0

        while i < n:
            if i + 2 < n and s[i + 2] == "#":
                res += m[s[i:i + 3]]
                i += 3
            else:
                res += m[s[i]]
                i += 1
        return res

