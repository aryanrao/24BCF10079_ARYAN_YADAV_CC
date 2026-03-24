class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = 0
        for each_num in nums:
            total_sum = total_sum + each_num

        remainder_needed = total_sum % p
        if remainder_needed == 0:
            return 0

        prefix_sum = 0
        remainder_index_map = {0: -1}

        smallest_length = len(nums)

        for index in range(len(nums)):
            prefix_sum = prefix_sum + nums[index]
            current_remainder = prefix_sum % p
            target_remainder = (current_remainder - remainder_needed) % p

            if target_remainder in remainder_index_map:
                prev_index = remainder_index_map[target_remainder]
                subarray_length = index - prev_index
                if subarray_length < smallest_length:
                    smallest_length = subarray_length

            remainder_index_map[current_remainder] = index

        if smallest_length == len(nums):
            return -1

        return smallest_length
        
