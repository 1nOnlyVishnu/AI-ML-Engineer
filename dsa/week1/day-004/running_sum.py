# Given an array nums. We define a running sum of an array as 
# runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

def runningSum(nums: list[int])-> list[int]:
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]
    return nums

print(runningSum([3,1,2,10,1]))

        
