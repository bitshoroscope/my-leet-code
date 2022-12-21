package com.bitshoroscope.issubsequence;


import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class TestIsSubsequenceSolution {

  Solution solution = new Solution();

  @Test
  public void testOk(){
    String s = "abc";
    String t = "ahbgdc";

    Assertions.assertTrue(solution.isSubsequence(s, t));
  }

  @Test
  public void testFalse(){
    String s = "axc";
    String t = "ahbgdc";
    Assertions.assertFalse(solution.isSubsequence(s, t));
  }

}
