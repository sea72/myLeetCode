class Solution0:
    def reverseWords(self, s: str) -> str:
        words = []
        slow, fast = 0, 0
        while fast < len(s) and slow < len(s):
            while slow < len(s) and s[slow] == ' ':
                slow += 1
            fast = slow
            while fast < len(s) and s[fast] != ' ':
                fast += 1
            if slow >= len(s):
                break
            if fast >= len(s):
                words.append(s[slow:])
                break
            else:
                words.append(s[slow:fast])
                slow = fast + 1
        return ' '.join(words[::-1])


class Solution1:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        s = s.strip()
        temp = []
        cur = 0
        while cur < len(s):
            if s[cur] == ' ' and temp:
                words.append(''.join(temp))
                temp.clear()
            elif s[cur] != ' ':
                temp.append(s[cur])
            cur += 1
        words.append(''.join(temp))
        return ' '.join(words[::-1])

sol = Solution()
print(sol.reverseWords("  hello    world  "))

