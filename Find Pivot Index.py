class Solution(object):
    def pivotIndex(self, nums):
        result = [nums[0]]
        for i in range(1,len(nums)):
            result.append(nums[i]+result[-1])
        l = 0
        for i in range(len(nums)):
            if l == result[len(nums)-1]- result[i]:
                return i
            l = result[i]
        return -1

