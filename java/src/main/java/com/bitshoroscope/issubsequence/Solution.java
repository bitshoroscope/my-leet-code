package com.bitshoroscope.issubsequence;

public class Solution {
  public boolean isSubsequence(String s, String t) {
    boolean result = false;
    int i = 0;
    int j = 0;
    String res = "";
    while(i < s.length() && j < t.length()){
      if (s.charAt(i) == t.charAt(j)){
        res += s.charAt(i);
        i++;
        j++;
      }
      else {
        j++;
      }
    }
    if(res.equals(s))
      result = true;
    return result;
  }
}
