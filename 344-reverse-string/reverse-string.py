class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n):
            temp = s[i]
            s[i] =  s[n - 1 - i]
            s[n - 1 - i] = temp

            if i >= n - 1 - i:
                return s
            elif i < n - 1 - i and i + 1 == n - 1 - i:
                return s
        
        