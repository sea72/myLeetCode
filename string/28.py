class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, -1
        next = [-1] * len(needle)
        while i < len(needle) - 1:
            if j == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                next[i] = j
            else:
                j = next[j]
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(needle):
            return i - j
        else:
            return -1

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return haystack.find(needle)


sol = Solution()
haystack = "abcdabcabced"
needle = "abcabce"
print(sol.strStr(haystack, needle))


