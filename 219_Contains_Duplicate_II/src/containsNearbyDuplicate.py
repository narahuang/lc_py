class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        map = {}
        for i, num in enumerate(nums):
            if num in map and i - map[num] <= k:
                return True
            map[num] = i
        return False
