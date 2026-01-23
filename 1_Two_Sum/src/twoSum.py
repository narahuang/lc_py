class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        result = []
        for i, num in enumerate(nums):
            diff_map[i] = (num, target - num)
        for key, value in diff_map.items():
            if value[1] in nums:
                result.append(key)
        if len(result) > 2:
            for result_num in result:
                if nums[result_num] * 2 == target:
                    result.remove(result_num)
        result.sort()
        return result
