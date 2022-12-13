from typing import List

class Solution:
  def runningSum(self, nums: List[int]) -> List[int]:
    accum = 0
    res = []
    for i in range (len(nums)):
      accum = accum + nums[i]
      res.append(accum)
    return res


