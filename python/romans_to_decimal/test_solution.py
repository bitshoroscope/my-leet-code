from solution import Solution as sol

def test_solution():
  assert 1 == sol.romanToInt(sol, "I")
  assert 4 == sol.romanToInt(sol, "IV")
  assert 9 == sol.romanToInt(sol, "IX")
  assert 99 == sol.romanToInt(sol, "XCIX")
  assert 1999 == sol.romanToInt(sol, "MCMXCIX")
