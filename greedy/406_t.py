from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key= lambda a:(a[0], -a[1]), reverse=True)
        res = []
        for person in people:
            res.insert(person[1], person)
        return res

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda a:(a[0], -a[1]))
        res = [[] for i in range(len(people))]
        for person in people:
            posForEmpty = 0
            for no in range(len(people)):
                if posForEmpty == person[1] and res[no] == []:
                    res[no] = person
                    break
                elif res[no] == []:
                    posForEmpty += 1
        return res



sol = Solution()
print(sol.reconstructQueue(people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))