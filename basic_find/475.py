from typing import List
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def isQualify(radius):
            warmSet = ()
            for heater in heaters:
                warmSet |= set(range(heater - radius, heater + radius + 1))
            for house in houses:
                if house not in warmSet:
                    return False
            return True
        
        

