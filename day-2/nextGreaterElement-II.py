#leetcode(503)--->Next Greater Element II
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        stack = []
        for i in range(n -1, -1, -1):
            stack.append(nums[i])
        result = [-1]*n

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
            stack.append(nums[i])
        return result
    
nums = [12, 10, 4, 15, 9, 200, 121, 154, 12]
#nums = list(map(int,input().split()))
