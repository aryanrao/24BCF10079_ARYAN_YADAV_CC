class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2
            current_sum = 0

            for each_num in nums:
                divided_value = (each_num + mid - 1) // mid
                current_sum = current_sum + divided_value

            if current_sum <= threshold:
                right = mid - 1
            else:
                left = mid + 1
        smallest_divisor = left
        return smallest_divisor
