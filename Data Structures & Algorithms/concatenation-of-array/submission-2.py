class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = [0] * (2 * len(nums))
        ans = []
        count = 2

        while count > 0:
            count = count-1
            for i in nums:
                ans.append(i)
                # ans[i] = nums[i]
                # ans[i+len(nums)] = nums[i]

        return ans