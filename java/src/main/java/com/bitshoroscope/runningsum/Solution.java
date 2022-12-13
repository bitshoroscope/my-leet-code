package com.bitshoroscope.runningsum;

public class Solution {
  public int[] runningSum(int[] nums) {
    int[] res = new int[nums.length];
    int accum = 0;
    for(int i = 0; i<nums.length; i++){
      accum += nums[i];
      res[i] = accum;
    }
    return res;
  }
}
