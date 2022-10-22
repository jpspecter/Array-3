#Time: O(n)
#Space: O(1)
#Program ran on leetcode successfully

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        n = len(nums)
        if k >= n:
            k = k % n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
    
    def reverse(self, nums, left, right):
        while (left <= right):
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left+= 1
            right += -1
            
        