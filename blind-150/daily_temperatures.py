"""
[MEDIUM] Daily Temperatures
__________________________

You are given an array of integers temperatures where temperatures[i]
represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the
ith day before a warmer temperature appears on a future day. If there is
no day in the future where a warmer temperature will appear for the ith day,
set result[i] to 0 instead.

"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = []

        for i, temp in enumerate(temperatures):
            days_after = 0
            greater = False
            for j, after in enumerate(temperatures[i+1:]):
                days_after += 1
                if (after > temp):
                    result.append(days_after)
                    greater = True
                    break
            
            if not greater:
                result.append(0)
                

        return result

                
 
Example_1 = Solution()
print(Example_1.dailyTemperatures(temperatures = [30,38,30,36,35,40,28]))

Example_2 = Solution()
print(Example_2.dailyTemperatures(temperatures = [22,21,20]))


"""
Examples:
__________________________
Example 1:

Input: temperatures = [30,38,30,36,35,40,28]
Output: [1,4,1,2,1,0,0]
----------

Example 2:

Input: temperatures = [22,21,20]
Output: [0,0,0]

"""