package com.bitshoroscope.runningsum;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

  @Test
  public void testSolution(){
    Solution sol = new Solution();
    int[] input = {1,2,3,4};
    int[] res = {1,3,6,10};
    assertArrayEquals(res, sol.runningSum(input));

    int[] input2 = {1,1,1,1,1};
    int[] res2 = {1,2,3,4,5};
    assertArrayEquals(res2, sol.runningSum(input2));

    int[] input3 = {3, 1, 2, 10, 1};
    int[] res3 = {3,4,6,16,17};
    assertArrayEquals(res3, sol.runningSum(input3));
  }
}
