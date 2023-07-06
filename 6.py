class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ["" for _ in range(numRows)]
        if numRows == 1:
            return s
        else:
            for index, word in enumerate(s):
                des = index % (2 * numRows -2)
                if des > numRows - 1:
                    rows[numRows - 1 - des % (numRows-1)] += word
                else:
                    rows[des % numRows] += word
            return "".join(rows)
            
ans = Solution()
print(ans.convert(s = "A", numRows = 3))

