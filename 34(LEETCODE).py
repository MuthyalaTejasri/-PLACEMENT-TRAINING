class Solution:
    def searchRange(self, nums, target):
        def binary_search(nums, target, find_first):
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    if find_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result

        first_occurrence = binary_search(nums, target, True)
        last_occurrence = binary_search(nums, target, False)
        return [first_occurrence, last_occurrence]