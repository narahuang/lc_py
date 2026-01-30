class Solution:
    def maxArea(self, height: list[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        max_area = 0
        while left_index < right_index:
            w = right_index - left_index
            h = min(height[left_index], height[right_index])
            max_area = max(w * h, max_area)
            if height[left_index] < height[right_index]:
                left_index += 1
            else:
                right_index -= 1
        return max_area
