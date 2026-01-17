"""
[MEDIUM] Container With Most Water
__________________________

Problem: You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container."""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0 # set initial area to 0
        # iterate through each pair of lines
        # calculate the area formed by the lines and update the maximum area found
        for x, h in enumerate(height):
            for y, h2 in enumerate(height[x+1:], start=x+1):
                temp_area = min(h, h2) * abs(y-x) # calculate area and ensure non-slanted container
                if temp_area > area:
                    area = temp_area
        return area

test = Solution()

# Test cases
print(test.maxArea(height = [1,8,6,2,5,4,8,3,7]))
print(test.maxArea(height = [1,1]))
