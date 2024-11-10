'''

Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false. There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

'''

# Optimal solution: O(n) -> Single traversal of array with comparisons

class Solution:
    def check(self, nums: List[int]) -> bool:

        rotationPoint = False
        rotationIdx = -1

        # Check if array is sorted, look for rotation point
        for i in range(len(nums)-1):
            if nums[i]<=nums[i+1]:
                continue
            else:
                rotationPoint = True
                rotationIdx = i+1
                break

        # If no rotation is found and sort condition is checked, return True
        if rotationPoint == False:
            return True

        # If the last element is the rotation idx, check if it is less than the first element
        if rotationIdx == len(nums)-1 and nums[-1]>nums[0]:
            return False

        # Check if the second half is sorted and if the elements are less than first half
        for i in range(rotationIdx, len(nums)-1):
            if nums[i]<=nums[i+1] and nums[i+1]<=nums[0]:
                continue
            else:
                return False

        return True
            
                

        