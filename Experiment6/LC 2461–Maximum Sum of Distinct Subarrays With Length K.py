class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        current_sum = 0
        seen = set()
        max_sum = 0
        
        for right in range(len(nums)):
            # Remove duplicates
            while nums[right] in seen:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            
            # Add current element
            seen.add(nums[right])
            current_sum += nums[right]
            
            # Maintain window size k
            if right - left + 1 > k:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            
            # Check valid window
            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum
        
